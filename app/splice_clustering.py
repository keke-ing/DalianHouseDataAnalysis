
import pandas as pd

from sklearn.cluster import KMeans

if __name__ == '__main__':

    df = pd.read_csv(
    r'/home/kekeing/Desktop/code/DateMining/data/lianjia_processed.csv', sep=',')
    dff = df[['deal_totalPrice', 'gross_area']]
    da = dff.to_numpy()


    k_means = KMeans(init='k-means++', n_clusters=3, n_init=22)
    k_means.fit(da)
    res0Series = pd.Series(k_means.labels_)

    res0 = res0Series[res0Series.values == 0]
    res1 = res0Series[res0Series.values == 1]
    res2 = res0Series[res0Series.values == 2]
    df_one = dff.iloc[res0.index]
    df_two = dff.iloc[res1.index]
    df_three = dff.iloc[res2.index]

    result_one = pd.merge(df_one, df, how='left',on=['deal_totalPrice', 'gross_area'])
    result_one.to_csv("../data/clustering_one.csv", index=False)

    result_two = pd.merge(df_two, df, how='left',on=['deal_totalPrice', 'gross_area'])
    result_two.to_csv("../data/clustering_two.csv", index=False)

    result_three = pd.merge(df_three, df, how='left',on=['deal_totalPrice', 'gross_area'])
    result_three.to_csv("../data/clustering_three.csv", index=False)


