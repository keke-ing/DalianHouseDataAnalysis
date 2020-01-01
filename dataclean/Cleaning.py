import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv(r'../data/chengjiao.csv', sep=',')

    # 打印原始基本信息
    print("original data rowCount: %d" % (df.shape[0]))
    print("original data colCount: %d" % (df.shape[1]))
    print(df.dtypes)

    # 去除Nan数据和重复数据
    df.dropna(inplace=True)
    df.drop_duplicates(keep="first", inplace=True)

    # 去除未知、暂无数据、车位、别墅
    df = df[df["build_year"] != "未知"]
    df = df[df["gross_area"] != "暂无数据"]
    df = df[df["house_orientation"] != "暂无数据"]
    df = df[df["with_elevator"] != "暂无数据"]
    df = df[df["year_of_property"] != "未知"]
    df = df[(df["household_style"] != "车位") & (df["household_style"] != "别墅")]
    # df = df[df["deal_time"].str.len() <= 10]

    # 打印清洗后的基本信息
    print("cleaned data rowCount: %d" % (df.shape[0]))
    print("cleaned data colCount: %d" % (df.shape[1]))

    # 输出清洗完成的数据
    df.to_csv("../data/lianjia_cleaned.csv", index=False)
