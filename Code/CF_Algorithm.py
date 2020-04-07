'''
UserCF : 基于用户的协同过滤算法
步骤：
1）找到和目标用户兴趣相似的用户集合  :   计算相似度！
2）找到这个集合中的用户喜欢的，且目标用户没有听说过的（接触过）物品推荐给目标用户
 '''

## 余弦相似度计算
## 复杂度 O(N²)
import math


def UserSimilarity(train):
    W =dict()
    for u in train.keys():
        for v in train.keys():
            if u== v:
                continue
            W[u][v] = len(train[u] & train[v])
            W[u][v] /= math.sqrt(len(train[u])  *  len(train[v])* 1.0 )
    return W


## 引入倒排表

def UserSimilarity(train):
    #建立倒排表

