<<<<<<< HEAD
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
=======
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as math

numbers = [1,2,3,11,12,13]
numSeries = pd.Series(numbers)
print(numSeries)
print(numSeries > 10)
print(numSeries %2 == 1)
print(numSeries.where(numSeries > 10).dropna())
print(numSeries.where(numSeries %2 == 1).dropna())
numbersGreater10 = numSeries > 10
numbersOdd = numSeries % 2 == 1
print(numSeries.where(numbersGreater10 & numbersOdd))
print(numSeries.where(numbersGreater10 & numbersOdd).dropna())
print(numSeries.between(3,12))
print(numSeries.where(numSeries.between(3,12)))
valuesToShow = numSeries.between(3,12)
print(numSeries.where(valuesToShow).dropna())


namesList = ['Albania','Austria','Belarus',
'Belgium','Bulgaria','Croatia','Cyprus','Czech Republic','Denmark','Estonia',
'Finland','France','Germany','Greece','Hungary','Iceland','Ireland','Italy',
'Latvia','Lithuania','Luxembourg','Macedonia','Malta','Montenegro','Netherlands',
'Norway','Poland','Portugal','Romania','Russia','Serbia','Slovenia','Spain', 'Sweden','Switzerland',
'United Kingdom','Turkey','Ukraine']

energy2010List = [1947,8347,3564,8369,4560,3814,4623,6348,6328,6506,16483,7736,7264,5318,3876,
51440,5911,5494,3230,3471,16830,3521,4171,5420,7010,24891,3797,4959,2551,
6410,4359,6521,5707,14934,8175,2498,3550,5701]

energy2012List  = [2118,8507,3698,7987,4762,3819,4057,6305,6039,6689,15687,7344,7270,5511,3919,
53203,5665,5398,3588,3608,14696,3626,4761,5416,6871,23658,3899,4736,2604,
6617,4387,6778,5573,14290,7886,2794,3641,5452]

namesSeries = pd.Series(namesList)
energy2010Series = pd.Series(energy2010List)
energy2012Series = pd.Series(energy2012List)
print(namesSeries)
print(energy2010Series)
print(energy2012Series)
mean2010 = energy2010Series.mean()
print(mean2010)
mean2012 = energy2012Series.mean()
print(mean2012)
filterAboveMean2010 = energy2010Series > mean2010
filterAboveMean2012 = energy2012Series > mean2012
print(namesSeries.where(filterAboveMean2010 & filterAboveMean2012).dropna())
filterBelowMean2010 = energy2010Series < mean2010
print(numSeries.where(filterBelowMean2010 & filterAboveMean2012).dropna())
>>>>>>> 57d1785 (Initial commit)
