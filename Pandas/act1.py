import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option('display.max_rows', 5)

print(reviews.country)

print(reviews['country'])

print(reviews.iloc[0])

print(reviews.iloc[:, 0])

print(reviews.iloc[1:3, 0])


print(reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']])

print(reviews.country == 'Italy')

print(reviews.loc[reviews.country == 'Italy'])

print(reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]) #or |

print(reviews.loc[reviews.country.isin(['Italy', 'France'])])