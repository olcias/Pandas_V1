import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as math
import random as rd

#pd.set_option('display.max_columns', None)

frame = pd.read_csv('/Users/olazielinska/Desktop/Pandas/course-files/Mcdonalds.csv')
series = pd.read_csv('/Users/olazielinska/Desktop/Pandas/course-files/Mcdonalds.csv',usecols=['Item','Calories'],index_col='Item').squeeze()

print(frame.head())
print(series.head())

print(series.count())
print(frame.count())

print(len(series))
print(len(frame))

print(series.dtypes)
print(frame.dtypes)

print(frame.dtypes.value_counts())

print(series.shape)
print(frame.shape)

print(series.axes)
print(frame.axes)

print(series.index)
print(frame.index)

print(frame.columns)

print(series.values)
print(frame.values)
print('/n')
print(series.info())
print('/n')
print(frame.info())

print(series.value_counts())
print(frame['Category'].value_counts())

print(series.sample())
print(frame.sample(n=3,axis='columns').head())
print(frame.sample(frac=0.02))