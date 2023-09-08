import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

#Ejercicio 1 --------------------------------
print(reviews_written = reviews.groupby('taster_twitter_handle').size())


#Ejercicio 2 --------------------------------
print(best_rating_per_price = reviews.groupby('price')['points'].max().sort_index())


#Ejercicio 3 --------------------------------
print(price_extremes = reviews.groupby('variety').price.agg([min, max]))


#Ejercicio 4 --------------------------------
print(sorted_varieties = price_extremes.sort_values(by=['min', 'max'], ascending=False))


#Ejercicio 5 --------------------------------
print(reviewer_mean_ratings = reviews.groupby('taster_name').points.mean())


#Ejercicio 6 --------------------------------
print(country_variety_counts = reviews.groupby(['country', 'variety']).size().sort_values(ascending=False))