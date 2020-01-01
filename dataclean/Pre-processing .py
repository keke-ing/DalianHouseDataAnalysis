import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv(r'../data/lianjia_cleaned.csv', sep=',')

    # 打印原始基本信息
    print("original data rowCount: %d" % (df.shape[0]))
    print("original data colCount: %d" % (df.shape[1]))
    print(df.dtypes)

    # 去除无用数据列
    df.drop("year_of_property", axis=1, inplace=True)  # 房屋年限
    # df.drop(["deal_time"], axis=1, inplace=True)

    # 特征数值化
    df.replace({"with_elevator": "无"}, 0, inplace=True)
    df.replace({"with_elevator": "有"}, 1, inplace=True)
    df.replace({"is_two_five": "暂无数据"}, 0, inplace=True)
    df.replace({"is_two_five": "满两年"}, 2, inplace=True)
    df.replace({"is_two_five": "满五年"}, 5, inplace=True)
    df.loc[:, "gross_area"] = df["gross_area"].str.strip("㎡")

    # 房屋户型
    # df[['bedroom', 'living_room', 'kitchen', 'toilet']] = df["household_style"].str.extract('(\d+)室(\d+)厅(\d+)厨(\d+)卫',
    #                                                                                  expand=False)
    lon = []
    lat = []
    la_lo = df['longitude_latitude']
    for i in la_lo:
        lon.append(i.split(',')[-2] )
        lat.append(i.split(',')[-1] )
    df['lon'] = lon
    df['lat'] = lat
    # df.drop("longitude_latitude", axis=1, inplace=True)

    # 楼层
    df["floor_number"] = df["floor_number"].str.extract('共(\d+)层', expand=False)

    # 建筑年限转为楼龄
    df["build_year"] = df["build_year"].map(lambda x: 2020 - int(x))
    df.rename(columns={'build_year': 'house_age'}, inplace=True)

    print("processed data rowCount: %d" % (df.shape[0]))
    print("processed data colCount: %d" % (df.shape[1]))

    # 写文件
    df.to_csv("../data/lianjia_processed.csv", index=False)
