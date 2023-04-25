import pandas as pd
import matplotlib.pyplot as plt

# read the data from the CSV file
df = pd.read_csv('data.csv')

# convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

# select only the rows that correspond to fruits
vegetable_df = df[df['category'] == 'vegetable']

# group the data by year and item
grouped = vegetable_df.groupby([pd.Grouper(key='date', freq='Y'), 'item'])

#grouping by date column at year frequency

# calculate the yearly inflation rate for each group
inflation_rates = []
for name, group in grouped:
    if len(group) > 1:
        prev_price = group['price'].iloc[0]
        for index, row in group.iterrows():
            curr_price = row['price']
            inflation_rate = (curr_price - prev_price) / prev_price
            inflation_rates.append({
                'year': name[0].year,
                'item': row['item'],
                'inflation_rate': inflation_rate
            })
            prev_price = curr_price


# create a DataFrame from the inflation_rates list
inflation_df = pd.DataFrame(inflation_rates)

# calculate the mean inflation rate per year
mean_inflation_df = inflation_df.groupby('year')['inflation_rate'].mean().reset_index()

vegetables = df[df['category'] == 'vegetable']
grouped = vegetables.groupby([pd.Grouper(key='date', freq='Y'), 'item'])

inflation_rates = []
for name, group in grouped:
    if len(group) > 1:
        prev_price = group['price'].iloc[0]
        for index, row in group.iterrows():
            curr_price = row['price']
            inflation_rate = (curr_price - prev_price) / prev_price
            inflation_rates.append({
                'date': name[0],
                'item': row['item'],
                'inflation_rate': inflation_rate
            })
            prev_price = curr_price

inflation_df = pd.DataFrame(inflation_rates)
p=inflation_df.max()
print(p)
q=inflation_df.min()
print(q)
