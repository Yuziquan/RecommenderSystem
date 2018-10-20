# 代码说明：
# 根据"D:\Recommender Systems\用户A/B/C对于其三个月来所看过节目的评分.xls"
# 生成"D:\Recommender Systems\所有用户看过的节目及所属类型的01矩阵.xlsx"
import pandas as pd
import numpy as np

if __name__ == '__main__':

    all_users_names = ['A', 'B', 'C']

    # 所有用户看过的节目名 all_items_users_saw = [item2, item3, item4]
    # 所有用户看过的节目名对应的类型 all_items_users_saw_labels = ["label2 label3", "label3", ...]
    all_items_users_saw = []
    all_items_users_saw_labels = []

    for j in range(len(all_users_names)):

        fileToBeRead = "D:\Recommender Systems\用户" + all_users_names[j] + "对于其三个月来所看过节目的评分.xls"
        df = pd.read_excel(fileToBeRead)
        (m, n) = df.shape
        data_array = np.array(df)

        for i in range(m):
            # 不重复记录相同的节目
           if data_array[i][2] not in all_items_users_saw:
               all_items_users_saw.append(data_array[i][2])
               all_items_users_saw_labels.append(data_array[i][3])

    # 生成"所有用户看过的节目及所属类型的01矩阵"
    all_labels = ['教育', '戏曲', '悬疑', '科幻', '惊悚', '动作', '资讯', '武侠', '剧情', '警匪', '生活', '军事', '言情', '体育', '冒险', '纪实', '少儿教育', '少儿', '综艺', '古装', '搞笑', '广告']
    labels_num = len(all_labels)

    all_items_labels_01_vectors = []

    for i in range(len(all_items_users_saw)):
        vector = [0] * labels_num
        labels_names = all_items_users_saw_labels[i].split(" ")

        for j in range(len(labels_names)):
            location = all_labels.index(labels_names[j])
            vector[location] = 1

        all_items_labels_01_vectors.append(vector)

    df = pd.DataFrame(all_items_labels_01_vectors, index=all_items_users_saw, columns=all_labels)
    df.to_excel("D:\Recommender Systems\所有用户看过的节目及所属类型的01矩阵.xlsx")

    # PS: 记得在生成的“所有用户看过的节目及所属类型的01矩阵表”中节目名那一列的首个空白的单元格中打上“节目名”