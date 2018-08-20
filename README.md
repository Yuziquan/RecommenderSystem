## RecommenderSystem

> 详情移步：https://blog.csdn.net/WuchangI/article/details/80160566

### 一、项目功能

实现一个网络电视节目推荐系统，基于每位用户的观看记录以及节目信息，对每位用户实行节目的个性化推荐。 主要技术是基于用户协同过滤与基于内容的推荐算法的后融合。

<br/>

***

### 二、项目运行效果

#### 1. 用户A(B、C)对于其三个月来所看过节目的评分

![1](https://github.com/Yuziquan/RecommenderSystem/blob/master/Screenshots/%E7%94%A8%E6%88%B7A(B%E3%80%81C)%E5%AF%B9%E4%BA%8E%E5%85%B6%E4%B8%89%E4%B8%AA%E6%9C%88%E6%9D%A5%E6%89%80%E7%9C%8B%E8%BF%87%E8%8A%82%E7%9B%AE%E7%9A%84%E8%AF%84%E5%88%86.png)

<br/>

#### 2. 备选推荐节目集及所属类型

![2](https://github.com/Yuziquan/RecommenderSystem/blob/master/Screenshots/%E5%A4%87%E9%80%89%E6%8E%A8%E8%8D%90%E8%8A%82%E7%9B%AE%E9%9B%86%E5%8F%8A%E6%89%80%E5%B1%9E%E7%B1%BB%E5%9E%8B.png)

<br/>

#### 3. 备选推荐节目集及所属类型01矩阵 

![3](https://github.com/Yuziquan/RecommenderSystem/blob/master/Screenshots/%E5%A4%87%E9%80%89%E6%8E%A8%E8%8D%90%E8%8A%82%E7%9B%AE%E9%9B%86%E5%8F%8A%E6%89%80%E5%B1%9E%E7%B1%BB%E5%9E%8B01%E7%9F%A9%E9%98%B5.png)

<br/>

#### 4. 所有用户对其看过的节目的评分矩阵 

![4](https://github.com/Yuziquan/RecommenderSystem/blob/master/Screenshots/%E6%89%80%E6%9C%89%E7%94%A8%E6%88%B7%E5%AF%B9%E5%85%B6%E7%9C%8B%E8%BF%87%E7%9A%84%E8%8A%82%E7%9B%AE%E7%9A%84%E8%AF%84%E5%88%86%E7%9F%A9%E9%98%B5.png)

<br/>

#### 5. 所有用户看过的节目及所属类型的01矩阵 

![5](https://github.com/Yuziquan/RecommenderSystem/blob/master/Screenshots/%E6%89%80%E6%9C%89%E7%94%A8%E6%88%B7%E7%9C%8B%E8%BF%87%E7%9A%84%E8%8A%82%E7%9B%AE%E5%8F%8A%E6%89%80%E5%B1%9E%E7%B1%BB%E5%9E%8B%E7%9A%8401%E7%9F%A9%E9%98%B5.png)

<br/>

#### 6. 基于内容的推荐算法CB的推荐结果 

![6](https://github.com/Yuziquan/RecommenderSystem/blob/master/Screenshots/CB_result.png)

<br/>
#### 7. 基于用户的协同过滤算法UserCF的推荐结果 

![7](https://github.com/Yuziquan/RecommenderSystem/blob/master/Screenshots/UserCF_result.png)

<br/>

#### 8. 将CB和UserCF的两个推荐集按一定比例混合(后融合)，实现混合推荐 

![8](https://github.com/Yuziquan/RecommenderSystem/blob/master/Screenshots/CB_Mixture_userCF_result.png)

