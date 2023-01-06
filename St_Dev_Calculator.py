import math

def variance(data):

    n = len(data)

    mean = sum(data) / n

    deviations = [(x - mean) ** 2 for x in data]

    variance = sum(deviations) / n

    return variance

def stdev(data):

    var = variance(data)

    std_dev = math.sqrt(var)
    
    return std_dev

listnums = [1, 2, 3, 4, 5, 6] # You can change the numbers between the "[]"

var = variance(listnums)
std = stdev(listnums)

print("variance = ", var)
print("Standard Deviation = ", std)