import pandas as pd
# # Test to ensure the pandas library was properly downloaded.
# data = pd.Series([1,2,3])
# data_2 = pd.DataFrame({'a': [1,2,3,4,5]})
# print (data, data_2)

#Step 1
# To preview the raw data.
january = pd.read_parquet ('/Users/elijahcapers/Dropbox/Baruch College/Summer 23/CIS 4400 Data Warehousing for Analytics/Term Project/Raw_Data/Yellow/Parquet/yellow_tripdata_2023-01.parquet', engine = 'auto')
february = pd.read_parquet ('/Users/elijahcapers/Dropbox/Baruch College/Summer 23/CIS 4400 Data Warehousing for Analytics/Term Project/Raw_Data/Yellow/Parquet/yellow_tripdata_2023-02.parquet', engine = 'auto')
march = pd.read_parquet ('/Users/elijahcapers/Dropbox/Baruch College/Summer 23/CIS 4400 Data Warehousing for Analytics/Term Project/Raw_Data/Yellow/Parquet/yellow_tripdata_2023-03.parquet', engine = 'auto')

# print(january)

# #Step 2
# # To convert the raw data from parquet to csv.
# yellow_df_1 = january
# yellow_df_1.to_csv('yellow_tripdata_2023-01.csv')

# yellow_df_2 = february
# yellow_df_2.to_csv('yellow_tripdata_2023-02.csv')

# yellow_df_3 = march
# yellow_df_3.to_csv('yellow_tripdata_2023-03.csv')

# # Step 3
# #Need to merge all files using concatenation.
# df = pd.concat (
#     map(pd.read_csv, ['yellow_tripdata_2023-01.csv', 'yellow_tripdata_2023-02.csv', 'yellow_tripdata_2023-03.csv' ]), ignore_index=False)
# df.to_csv('all_yellow_tripdata_2023.csv')

# all = pd.read_csv ('all_yellow_tripdata_2023.csv')
# print(all)

