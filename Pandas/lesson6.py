#1

renamed = reviews.rename(columns=dict(region_1='region', region_2='locale'))

# Check your answer
q1.check()


#2

reindexed = reviews.rename_axis('wines', axis='rows')

# Check your answer
q2.check()


#3

combined_products = pd.concat([gaming_products, movie_products])

# Check your answer
q3.check()


#4

powerlifting_combined = powerlifting_meets.set_index("MeetID").join(powerlifting_competitors.set_index("MeetID"))

# Check your answer
q4.check()
