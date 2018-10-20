# 代码说明：
# 根据"D:\Recommender Systems\备选推荐节目集及所属类型.xlsx"生成"D:\Recommender Systems\备选推荐节目集及所属类型01矩阵.xlsx"

import pandas as pd
import numpy as np

if __name__ == '__main__':

    df = pd.read_excel("D:\Recommender Systems\备选推荐节目集及所属类型.xlsx")
    (m, n) = df.shape

    data_array = np.array(df.iloc[0:m+1,:])
    print(data_array)

    # 按指定顺序排列的所有标签
    all_labels = ['教育', '戏曲', '悬疑', '科幻', '惊悚', '动作', '资讯', '武侠', '剧情', '警匪', '生活', '军事', '言情', '体育', '冒险', '纪实', '少儿教育', '少儿', '综艺', '古装', '搞笑', '广告']
    labels_num = len(all_labels)

    # 按顺序提取所有节目的名称
    all_items_names = np.array(df.iloc[:m+1, 0])
    print(all_items_names)

    # 创建一个01矩阵，0表示该节目不属于该类型，1表示该节目属于该类型
    data_to_be_written = []

    for i in range(len(all_items_names)):

        # 每个节目的01行向量
        vector = [0] * labels_num
        labels_names = str(data_array[i][1]).split(" ")

        for j in range(len(labels_names)):
            location = all_labels.index(labels_names[j])
            vector[location] = 1

        data_to_be_written.append(vector)

    # 将01矩阵写入“备选推荐节目集及所属类型01矩阵”
    df = pd.DataFrame(data_to_be_written, index=all_items_names, columns=all_labels)
    df.to_excel("D:\Recommender Systems\备选推荐节目集及所属类型01矩阵.xlsx")

    # PS: 记得在生成的“备选推荐节目集及所属类型01矩阵表”中节目名那一列的首个空白的单元格中打上“节目名”



























