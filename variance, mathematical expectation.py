#a**0.5  = رادیکال
from statistics import *
a = [int(i) for i in input("Enter your numbers for calculate sample variance:").split()]
print(variance(a))

import numpy
s = [int(i) for i in input("Enter your numbers for calculate population variance:").split()]
print(numpy.var(s))


#https://picuki.me/pesarkoni68/
#POWERED BY SALEH AMOO
import numpy as saleh
def calculateExpectedValue(values, weights):
    values = saleh.asarray(values)
    weights = saleh.asarray(weights)
    return (values * weights).sum() / weights.sum()
score = [float(i) for i in input("Enter your numbers for calculate mathematical expectation:").split()]
chance = [(score[0]/len(score))*(len(score)) for i in range(len(score))]

expected_value = calculateExpectedValue(score, chance)
print("The expected value is :", expected_value)