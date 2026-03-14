import pandas as pd
from keras.src.layers import average

df = pd.read_cvs('file1.csv')
print(df.info())


first_rows = df.head()
print(first_rows)


country_data = df['Country']
print(country_data)



subset =df[['Country','Average IQ']]
print(subset)


filtered_df = subset[subset['Average IQ'] > 100]
print(filtered_df)

duplicated_count = df.duplicate().sum()


print("\nCount of duplicate rows:")
print(duplicated_count)


 average_iq_per_continent = df.groupby('Continent')['Average IQ'].mean()
 print(average_iq_per_continent)