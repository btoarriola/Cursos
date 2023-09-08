#1

desc = reviews.description

# Check your answer
q1.check()


#2

first_description = reviews.description.iloc[0]

# Check your answer
q2.check()
first_description


#3

first_row = reviews.iloc[0]

# Check your answer
q3.check()
first_row


#4

first_descriptions = reviews.description.iloc[:10]

# Check your answer
q4.check()
first_descriptions


#5

indices = [1, 2, 3, 5, 8]
sample_reviews = reviews.loc[indices]

# Check your answer
q5.check()
sample_reviews


#6

cols = ['country', 'province', 'region_1', 'region_2']
indices = [0, 1, 10, 100]
df = reviews.loc[indices, cols]

# Check your answer
q6.check()
df


#7

cols = ['country', 'variety']
df = reviews.loc[:99, cols]
# Check your answer
q7.check()
df


#8

italian_wines = reviews[reviews.country == 'Italy']

# Check your answer
q8.check()


#9

top_oceania_wines = reviews.loc[(reviews.country.isin(['Australia', 'New Zealand']))& (reviews.points >= 95)]

# Check your answer
q9.check()
top_oceania_wines
