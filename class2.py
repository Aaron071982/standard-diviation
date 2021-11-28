import csv
import math

with open("class2.csv", newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

data = file_data[0]

#mean
def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total += int(x)

    mean = total/n
    return mean


#squaring values
squared_list = []
for number in data:
    a  = int(number) - mean(data)
    a = a**2
    squared_list.append(a)

#getting sum
sum = 0
for i in squared_list:
    sum = sum+i

#diving sum for total values
result = sum/(len(data)-1)

#getting the deviations
std_deviation = math.sqrt(result)
print(std_deviation)

