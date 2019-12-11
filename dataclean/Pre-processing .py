import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv(r'../data/lianjia_cleaned.csv', sep=',')

    # 打印原始基本信息
    print("original data rowCount: %d" % (df.shape[0]))
    print("original data colCount: %d" % (df.shape[1]))
    print(df.dtypes)

    # 去除无用数据列
    # df.drop("house_usage", axis=1, inplace=True)  # 房屋用途
    df.drop("year_of_property", axis=1, inplace=True)  # 房屋年限
    # df.drop(["deal_time"], axis=1, inplace=True)

    # 特征数值化
    df.replace({"with_elevator": "无"}, 0, inplace=True)
    df.replace({"with_elevator": "有"}, 1, inplace=True)
    df.replace({"is_two_five": "暂无数据"}, 0, inplace=True)
    df.replace({"is_two_five": "满两年"}, 2, inplace=True)
    df.replace({"is_two_five": "满五年"}, 5, inplace=True)
    df.loc[:, "gross_area"] = df["gross_area"].str.strip("㎡")

    # 房屋朝向的数值化
    df_house_orientation_group = df.groupby(by='house_orientation')
    house_orientation_list = list(df_house_orientation_group.groups.keys())

    house_orientation_dict = {"东南": 2, "南": 3, "西南": 1, "西": -1, "西北": -1.5, "北": -2, "东北": 0, "东": 1}


    # 将li中的房屋朝向，通过索引dic的方式转换为权重值val
    def split_house_orientation_list(*li, **dic):
        lis = []
        for it in li:
            v = 0
            for k in it.split():
                if k in dic.keys():
                    v += dic[k]  # 累加所有朝向的组合分数
            lis.append(v)
        return lis


    # 房屋朝向权重列表
    house_orientation_data = split_house_orientation_list(*house_orientation_list, **house_orientation_dict)

    # 房屋朝向替换为权重值val
    for item, val in zip(df_house_orientation_group.groups.keys(), house_orientation_data):
        df.replace({"house_orientation": item}, val, inplace=True)

    # 房屋户型
    df[['bedroom', 'living_room', 'kitchen', 'toilet']] = df["household_style"].str.extract('(\d+)室(\d+)厅(\d+)厨(\d+)卫',
                                                                                            expand=False)
    df.drop("household_style", axis=1, inplace=True)

    # 楼层
    df["floor_number"] = df["floor_number"].str.extract('共(\d+)层', expand=False)

    # 建筑年限转为楼龄
    df["build_year"] = df["build_year"].map(lambda x: 2019 - int(x))
    df.rename(columns={'build_year': 'house_age'}, inplace=True)

    print("processed data rowCount: %d" % (df.shape[0]))
    print("processed data colCount: %d" % (df.shape[1]))

    # 写文件
    df.to_csv("lianjia_processed.csv", index=False)
