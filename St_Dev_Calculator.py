# Made by Mohammed Omar Al-Aidaroos and supervised by Mr. Mohammed Marhomy for the math project of grade 11.

import math


def variance(data):

    n = len(data)

    mean = sum(data) / n

    deviations = [(x - mean)**2 for x in data]

    variance = sum(deviations) / n

    return variance


def stdev(data):

    var = variance(data)

    std_dev = math.sqrt(var)

    return std_dev


listnums = [1, 2]  # You can change the numbers between the "[]"

result = len(listnums)
if result <= 1:
    print("Please add more numbers to your list.")

else:
    var = variance(listnums)
    std = stdev(listnums)
    print("variance = ", var)
    print("Standard Deviation = ", std)
