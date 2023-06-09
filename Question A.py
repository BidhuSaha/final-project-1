import pandas as pd
import matplotlib.pyplot as plt

# read the data from the CSV file
df = pd.read_csv('data.csv')

# convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')


# group the data by year and item
grouped=df.groupby([pd.Grouper(key='date', freq='Y'), 'item'])

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

# create a scatter plot of the mean inflation rate per year
plt.scatter(mean_inflation_df['year'], mean_inflation_df['inflation_rate'])
plt.plot(mean_inflation_df['year'], mean_inflation_df['inflation_rate'], color='red')
plt.xlabel('Year')
plt.ylabel('Mean Inflation Rate')
plt.title('Mean Inflation Rate ')
plt.show()

# print the inflation rate
print('Inflation rate:')
print(inflation_df)


#devide
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')


grouped = df.groupby([pd.Grouper(key='date', freq='Y'), 'item'])

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

fig, ax = plt.subplots()
for item in inflation_df['item'].unique():
    item_df = inflation_df[inflation_df['item'] == item]
    ax.scatter(item_df['date'], item_df['inflation_rate'], label=item)
    ax.plot(item_df['date'], item_df['inflation_rate'])

ax.set_xlabel('Year')
ax.set_ylabel('Inflation rate')
ax.set_title('Inflation rate of vegetable')
ax.legend()

plt.show()
