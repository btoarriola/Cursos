#1

median_points = reviews.points.median()

# Check your answer
q1.check()


#2

countries = reviews.country.unique()

# Check your answer
q2.check()


#3

reviews_per_country = reviews.country.value_counts()

# Check your answer
q3.check()


#4

centered_price = reviews.price - reviews.price.mean()

# Check your answer
q4.check()


#5

bargain_idx = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_idx, 'title']

# Check your answer
q5.check()


#6

n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])

# Check your answer
q6.check()


#7

def stars(row):
    if row.country == 'Canada':
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1

star_ratings = reviews.apply(stars, axis='columns')

# Check your answer
q7.check()

