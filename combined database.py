while True:
    print(f"\nChoose any of the options below:"
        "\nA:-Database"
        "\nB:-Question Regarding the Database"
        "\nC:-Quit/Exit")
    user_input= input("\n:").capitalize()
    if user_input=='C':
        print(f"\nUser exit.Thank You!")
        break
    elif user_input=='A':
        import pandas as pd
        data = pd.read_csv('data.csv')
        print(data)


        break
    elif user_input=='B':
        print(f"\nChoose any of the question below:"
              "\nQ(A) What is the change in inflation rate throughout years?"
              "\nQ(B) What is the Yearly inflation rate change of Vegetable?"
              "\nQ(C) What is the Yearly inflation rate change of fruits?"
              "\nQ(D) Which Vegetable was the most and least effected over the years?"
              "\nQ(E) Which Fruit was most and least effected over the year?"
              "\nQ(F) At what year was the most significant change in inflation?")
       
        user_question= input("\nQ:").capitalize()

        import pandas as pd 
        import matplotlib.pyplot as plt

        while True:
            if user_question=='A':
                print(f"\nInflation:"
                  "\n Inflation is an increase in the general price level of goods and services in an economy. When the general price level rises, each unit of currency buys fewer goods and services;consequently, inflation corresponds to a reduction in the purchasing power of money.")
                df = pd.read_csv('data.csv')
                df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
                grouped=df.groupby([pd.Grouper(key='date', freq='Y'), 'item'])
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
                                    'inflation_rate': inflation_rate})
                               prev_price = curr_price
                inflation_df = pd.DataFrame(inflation_rates)
                mean_inflation_df = inflation_df.groupby('year')['inflation_rate'].mean().reset_index()
                plt.scatter(mean_inflation_df['year'], mean_inflation_df['inflation_rate'])
                plt.plot(mean_inflation_df['year'], mean_inflation_df['inflation_rate'], color='red')
                plt.xlabel('Year')
                plt.ylabel('Mean Inflation Rate')
                plt.title('Mean Inflation Rate ')
                plt.show()
                print('Inflation rate:')
                print(inflation_df)
                pd['date'] = pd.to_datetime(pd['date'], format='%Y-%m-%d')
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
                                    'inflation_rate': inflation_rate})
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

            elif user_question=='B':
                df = pd.read_csv('data.csv')
                df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
                vegetable_df = df[df['category'] == 'vegetable']
                grouped = vegetable_df.groupby([pd.Grouper(key='date', freq='Y'), 'item'])
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
                                    'inflation_rate': inflation_rate})
                               prev_price = curr_price
                          
                inflation_df = pd.DataFrame(inflation_rates)
                mean_inflation_df = inflation_df.groupby('year')['inflation_rate'].mean().reset_index()
                plt.scatter(mean_inflation_df['year'], mean_inflation_df['inflation_rate'])
                plt.plot(mean_inflation_df['year'], mean_inflation_df['inflation_rate'], color='red')
                plt.xlabel('Year')
                plt.ylabel('Mean Inflation Rate')
                plt.title('Mean Inflation Rate of vegetable')
                plt.show()
                print('Inflation rate of vegetable:')
                print(inflation_df)
            
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
                                'inflation_rate': inflation_rate})
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
                
                vegetable_type = input("Enter the type of fruit to check its inflation rate: ")
                vegetable_df = df[df['item'] == vegetable_type]
                grouped = vegetable_df.groupby([pd.Grouper(key='date', freq='Y'), 'item'])
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
                                'inflation_rate': inflation_rate})
                            prev_price = curr_price
                inflation_df = pd.DataFrame(inflation_rates)
                mean_inflation_df = inflation_df.groupby('year')['inflation_rate'].mean().reset_index()
                plt.scatter(mean_inflation_df['year'], mean_inflation_df['inflation_rate'])
                plt.plot(mean_inflation_df['year'], mean_inflation_df['inflation_rate'], color='red')
                plt.xlabel('Year')
                plt.ylabel('Mean Inflation Rate')
                plt.title('Mean Inflation Rate of vegetable')
                plt.show()
                print('Inflation rate of vegetables:')
                print(inflation_df)
                break


            elif user_question=='C':
                 df = pd.read_csv('data.csv')
                 df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
                 fruit_df = df[df['category'] == 'fruit']
                 grouped = fruit_df.groupby([pd.Grouper(key='date', freq='Y'), 'item'])
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
                                    'inflation_rate': inflation_rate})
                               prev_price = curr_price
                          
                 inflation_df = pd.DataFrame(inflation_rates)
                 mean_inflation_df = inflation_df.groupby('year')['inflation_rate'].mean().reset_index()
                 plt.scatter(mean_inflation_df['year'], mean_inflation_df['inflation_rate'])
                 plt.plot(mean_inflation_df['year'], mean_inflation_df['inflation_rate'], color='red')
                 plt.xlabel('Year')
                 plt.ylabel('Mean Inflation Rate')
                 plt.title('Mean Inflation Rate of fruits')
                 plt.show()
                 print('Inflation rate of fruits:')
                 print(inflation_df)
            
                 fruits = df[df['category'] == 'fruit']
                 grouped = fruits.groupby([pd.Grouper(key='date', freq='Y'), 'item'])
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
                                'inflation_rate': inflation_rate})
                            prev_price = curr_price
                 inflation_df = pd.DataFrame(inflation_rates)
                 fig, ax = plt.subplots()
                 for item in inflation_df['item'].unique():
                     item_df = inflation_df[inflation_df['item'] == item]
                     ax.scatter(item_df['date'], item_df['inflation_rate'], label=item)
                     ax.plot(item_df['date'], item_df['inflation_rate'])
                 ax.set_xlabel('Year')
                 ax.set_ylabel('Inflation rate')
                 ax.set_title('Inflation rate of fruit')
                 ax.legend()
                 plt.show()
                
                 fruit_type = input("Enter the type of fruit to check its inflation rate: ")
                 fruite_df = df[df['item'] == fruit_type]
                 grouped = fruit_df.groupby([pd.Grouper(key='date', freq='Y'), 'item'])
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
                                'inflation_rate': inflation_rate})
                             prev_price = curr_price
                 inflation_df = pd.DataFrame(inflation_rates)
                 mean_inflation_df = inflation_df.groupby('year')['inflation_rate'].mean().reset_index()
                 plt.scatter(mean_inflation_df['year'], mean_inflation_df['inflation_rate'])
                 plt.plot(mean_inflation_df['year'], mean_inflation_df['inflation_rate'], color='red')
                 plt.xlabel('Year')
                 plt.ylabel('Mean Inflation Rate')
                 plt.title('Mean Inflation Rate of fruits')
                 plt.show()
                 print('Inflation rate of fruits:')
                 print(inflation_df)
                 break
                

            elif user_question=='D':
                
                df = pd.read_csv('data.csv')
                count=1
                df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
                vegetable_df = df[df['category'] == 'vegetable']
                grouped = vegetable_df.groupby([pd.Grouper(key='date', freq='Y'), 'item'])
                
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
                inflation_df = pd.DataFrame(inflation_rates)
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
                                    'inflation_rate': inflation_rate})
                               prev_price = curr_price

                inflation_df = pd.DataFrame(inflation_rates)
                p=inflation_df.max()
                print(p)
                q=inflation_df.min()
                print(q)
                plt.scatter(mean_inflation_df['year'], mean_inflation_df['inflation_rate'])
                plt.plot(mean_inflation_df['year'], mean_inflation_df['inflation_rate'], color='blue')
                plt.xlabel('Year')
                plt.ylabel('Mean Inflation Rate')
                plt.title('Mean Inflation Rate of vegetable')
                plt.show()
                
                
                break
                

                          
            elif user_question=='E':
                
                df = pd.read_csv('data.csv')
                df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
                vegetable_df = df[df['category'] == 'fruit']
                grouped = vegetable_df.groupby([pd.Grouper(key='date', freq='Y'), 'item'])
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
                                'inflation_rate': inflation_rate})
                            prev_price = curr_price
                inflation_df = pd.DataFrame(inflation_rates)
                mean_inflation_df = inflation_df.groupby('year')['inflation_rate'].mean().reset_index()
                vegetables = df[df['category'] == 'fruit']
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
                                'inflation_rate': inflation_rate})
                            prev_price = curr_price
                inflation_df = pd.DataFrame(inflation_rates)
                p=inflation_df.max()
                print(p)
                q=inflation_df.min()
                print(q)
                
                plt.scatter(mean_inflation_df['year'], mean_inflation_df['inflation_rate'])
                plt.plot(mean_inflation_df['year'], mean_inflation_df['inflation_rate'], color='green')
                plt.xlabel('Year')
                plt.ylabel('Mean Inflation Rate')
                plt.title('Mean Inflation Rate of fruits')
                plt.show()
                
                break
            elif user_question=='F':
                print(f"Inflation as measured by the consumer price index reflects the annual percentage change in the cost to the average consumer of acquiring a basket of goods and services that may be fixed or changed at specified intervals, such as yearly. The Laspeyres formula is generally used."
                        "\nU.K. inflation rate for 2022 was 3.78%, a 2.55% increase from 2022"
                        "\nU.K. inflation rate for 2022 was 2.52%, a 2.30% increase from 2021"
                        "\nU.K. inflation rate for 2021 was 2.32%, a 1.53% increase from 2020."
                        "\nU.K. inflation rate for 2020 was 0.99%, a 0.75% decline from 2019."
                        "\nU.K. inflation rate for 2019 was 1.74%, a 0.55% decline from 2018."
                        "\nU.K. inflation rate for 2018 was 2.29%, a 0.27% decline from 2017.")
                print(f"The most significant change in inflation  was on 2022")
                break
   
    else:
        print(f"Try Again(Error)")


    break
