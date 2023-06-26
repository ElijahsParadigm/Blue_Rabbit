import pandas as pd
# # Test to ensure the pandas library was properly downloaded.
# data = pd.Series([1,2,3])
# data_2 = pd.DataFrame({'a': [1,2,3,4,5]})
# print (data, data_2)

# Step 1
# To preview the raw data.
january = pd.read_parquet ('/Users/elijahcapers/Dropbox/Baruch College/Summer 23/CIS 4400 Data Warehousing for Analytics/Term Project/Raw_Data/Green/Parquet/green_tripdata_2023-01.parquet', engine = 'auto')
february = pd.read_parquet ('/Users/elijahcapers/Dropbox/Baruch College/Summer 23/CIS 4400 Data Warehousing for Analytics/Term Project/Raw_Data/Green/Parquet/green_tripdata_2023-02.parquet', engine = 'auto')
march = pd.read_parquet ('/Users/elijahcapers/Dropbox/Baruch College/Summer 23/CIS 4400 Data Warehousing for Analytics/Term Project/Raw_Data/Green/Parquet/green_tripdata_2023-03.parquet', engine = 'auto')

print(january, february, march)

# # Step 2
# # To convert the raw data from parquet to csv.
# green_df_1 = january
# green_df_1.to_csv('green_tripdata_2023-01.csv')

# green_df_2 = february
# green_df_2.to_csv('green_tripdata_2023-02.csv')

# green_df_3 = march
# green_df_3.to_csv('green_tripdata_2023-03.csv')

# # Step 3
# # Need to merge all files using concatenation.
# df = pd.concat (
#     map(pd.read_csv, ['green_tripdata_2023-01.csv', 'green_tripdata_2023-02.csv', 'green_tripdata_2023-03.csv' ]), ignore_index=False)
# df.to_csv('all_green_tripdata_2023.csv')

