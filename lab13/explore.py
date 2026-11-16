import pandas as pd; df =
pd.read_csv('data/retail_sales.csv')
print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

print("---exercise 2---")

south = df[df['region'] == 'South']
print(len(south))
print(south.head())

print("---exercise 3---")

df.sort_values('revenue', ascending=False).head(5)
print(df.sort_values)

print("---exercise 4---")

big_south = df[(df['region']=='South')]
(df['revenue']>1000)

print("---exercise 5---")

df['per_unit'] = df['revenue'] / df['quantity']
df['quantity']
print(df.head())

print("---exercise 6---")

# Method 1
print(df['region'].unique())
# Method 2
print(df['region'].value_counts())

print("---exercise 7---")



print("---exercise 8---")