#1

dtype = reviews.points.dtype

# Check your answer
q1.check()


#2

point_strings = reviews.points.astype(str)

# Check your answer
q2.check()


#3

missing_price_reviews = reviews[reviews.price.isnull()]
n_missing_prices = len(missing_price_reviews)
n_missing_prices = reviews.price.isnull().sum()

# Check your answer
q3.check()


#4

reviews_per_region = reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)

# Check your answer
q4.check()

