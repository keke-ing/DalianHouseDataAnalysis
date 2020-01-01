import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv(r'/data/lianjia_processed.csv', sep=',')
    district_number = df.district.value_counts().reset_index().sort_values(by='district', ascending=False)
