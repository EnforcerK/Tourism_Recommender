import random


# 分割数据集过程
# 分成M份数据，进行M此实验， 每次选取不同的K，每次使用相同的随机数种子
def SplitData(data, M, k, seed):
    test = []
    train = []
    random.seed(seed)
    for user, item in data:
        if random.randint(0, M) == k:
            test.append([user, item])
        else:
            train.append([user, item])
    return train, test

# 计算召回率: 描述有多少比例的用户-物品评分记录包含在最终的推荐列表中

def Recall(train, test, N):
    hit = 0
    all = 0
    for user in train.keys():
        tu = test[user]
        rank = getRecommendation(user, N)
        for item, pui in rank:
            if item in tu:
                hit+=1
        all += len(tu)
    return hit/(all*1.0)


# 计算准确率： 描述最终的推荐列表中有多少比例是发生过的用户-物品评分记录

def Precision(train, test, N):
    hit =0
    all =0
    for user in train.keys():
        tu =test[user]
        rank = GetRecommendation(user, N)
        for item, pui in rank:
            if item in tu:
                hit +=1
        all += N
    return hit/(all*1.0)


# 计算覆盖率： 简单定义：最终的推荐列表中包含多大比例的物品

def Coverage(train, test, N):
    recommend_items = set()
    all_items = set()
    for user in train.keys():
        for item in train[user].keys():
            all_items.add(item)
        rank = GetRecommendation(user, N)
        for item, pui in rank:
            recommend_items.add(item)
    return len(recommend_items) / (len(all_items)*1.0)