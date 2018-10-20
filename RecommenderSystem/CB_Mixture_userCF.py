from recommender_system.CB import *
from recommender_system.UserCF import *


# 输出推荐给该用户的节目列表
# max_num:最多输出的推荐节目数
def printRecommendItems(recommend_items_sorted, max_num):
    count = 0
    for item, degree in recommend_items_sorted:
        print("节目名：%s， 推荐指数：%f" % (item, degree))
        count += 1
        if count == max_num:
            break

if __name__ == '__main__':

    all_users_names = ['A', 'B', 'C']
    all_labels = ['教育', '戏曲', '悬疑', '科幻', '惊悚', '动作', '资讯', '武侠', '剧情', '警匪', '生活', '军事', '言情', '体育', '冒险', '纪实',
                  '少儿教育', '少儿', '综艺', '古装', '搞笑', '广告']
    labels_num = len(all_labels)

    df1 = pd.read_excel("D:\Recommender Systems\所有用户对其看过的节目的评分矩阵.xlsx")
    (m1, n1) = df1.shape
    # 所有用户对其看过的节目的评分矩阵
    # data_array1 = [[0.1804 0.042 0.11  0.07  0.19  0.56  0.14  0.3  0.32 0, ...], [...]]
    data_array1 = np.array(df1.iloc[:m1 + 1, 1:])
    # 按照"所有用户对其看过的节目的评分矩阵"的列序排列的所有用户观看过的节目名称
    items_users_saw_names1 = df1.columns[1:].tolist()

    # users_dict = {用户一:[['节目一', 3.2], ['节目四', 0.2], ['节目八', 6.5]], 用户二: ... }
    users_dict = createUsersDict(df1)
    # items_dict = {节目一: [用户一, 用户三], 节目二: [...], ... }
    items_dict = createItemsDict(df1)

    df2 = pd.read_excel("D:\Recommender Systems\所有用户看过的节目及所属类型的01矩阵.xlsx")
    (m2, n2) = df2.shape
    data_array2 = np.array(df2.iloc[:m2 + 1, 1:])
    # 按照"所有用户看过的节目及所属类型的01矩阵"的列序排列的所有用户观看过的节目名称
    items_users_saw_names2 = np.array(df2.iloc[:m2 + 1, 0]).tolist()

    # 为用户看过的节目建立节目画像
    items_users_saw_profiles = createItemsProfiles(data_array2, all_labels, items_users_saw_names2)

    # 建立用户画像users_profiles和用户看过的节目集items_users_saw
    (users_profiles, items_users_saw) = createUsersProfiles(data_array1, all_users_names, items_users_saw_names1,
                                                            all_labels, items_users_saw_profiles)

    df3 = pd.read_excel("D:\Recommender Systems\备选推荐节目集及所属类型01矩阵.xlsx")
    (m3, n3) = df3.shape
    data_array3 = np.array(df3.iloc[:m3 + 1, 1:])
    # 按照"备选推荐节目集及所属类型01矩阵"的列序排列的所有用户观看过的节目名称
    items_to_be_recommended_names = np.array(df3.iloc[:m3 + 1, 0]).tolist()

    # 为备选推荐节目集建立节目画像
    items_to_be_recommended_profiles = createItemsProfiles(data_array3, all_labels, items_to_be_recommended_names)


    # 两种推荐算法后融合，也就是将两种推荐算法对某个用户分别产生的两个推荐节目集按不同比例混合，得出最后的对该用户的推荐结果

    # 对于每个用户推荐topN个节目,在两种推荐算法产生的推荐集中分别选取比例为w1和w2的推荐结果,CB占w1, userCF占w2
    # w1 + w2 = 1 且 w1 * topN + w2 * topN = topN

    topN = 5

    w1 = 0.7
    w2 = 0.3

    # 从CB的推荐集中选出前topW1项
    topW1 = int(w1 * topN)

    # 从userCF的推荐集中选出前topW2项
    topW2 = topN-topW1

    for user in all_users_names:

        # 对于用户user的最终混合推荐节目集
        recommend_items = []

        # CB
        # recommend_items1 =  [[节目名, 该节目与该用户user画像的相似度], ...]
        recommend_items1 = contentBased(users_profiles[user], items_to_be_recommended_profiles, items_to_be_recommended_names, all_labels, items_users_saw[user])
        len1 = len(recommend_items1)

        if len1 <= topW1:
            recommend_items = recommend_items + recommend_items1
        else:
            recommend_items = recommend_items + recommend_items1[:topW1]


        # userCF
        # recommend_item2 = [[节目名, 该用户user对该节目的感兴趣程度],...]
        recommend_items2 = userCF(user, users_dict, items_dict, 2, items_to_be_recommended_names)
        len2 = len(recommend_items2)

        if len2 <= topW2:
            recommend_items = recommend_items + recommend_items2
        else:
            recommend_items = recommend_items + recommend_items2[:topW2]

        # 将推荐结果按推荐指数降序排序
        recommend_items.sort(key=lambda item: item[1], reverse=True)

        print("对于用户 %s 的推荐节目如下" % user)
        printRecommendItems(recommend_items, 5)
        print()