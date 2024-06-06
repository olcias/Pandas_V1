import pandas as pd
countries = pd.read_csv('/Users/olazielinska/Desktop/Pandas/course-files/countries.csv', usecols=['Symbol', 'Name'], index_col='Symbol')
countries = countries.squeeze()
print(countries.head(20))