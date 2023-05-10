# script to plot data capture from to oscilloscope

import matplotlib.pyplot as plt
import csv

OFFSET = 5


x = []
y = []
step = 0

# Reads csv file based on offset
with open('TEK00001.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    ct = 0
    for row in plots:
        ct += 1
        if ct == OFFSET :
            ct = 0
            x.append(float(row[0]))
            y.append(float(row[1]))

for yVal in y:
    if yVal < 16.2 :
        y[step] = 0
    else :
        y[step] = 1
    step += 1

step = 0

for xVal in x:
    x[step] = step
    step += 1

xMin = 124300
xMax = 266000

bitLength = (xMax - xMin) / 45
bitLengthInt = int(bitLength)
bitList = []

for i in range(45) :
    sum = 0
    for j in range(bitLengthInt):
        index = 124300 + (i * bitLengthInt) + j
        sum += y[index]
        rangeAvg = sum/bitLengthInt
    bitList.append(rangeAvg)

bitStep = 0
for bit in bitList:
    if bit < .03 or bit > 0.04:
        bitList[bitStep] = 0
    else:
        bitList[bitStep] = 1
    bitStep += 1

for i in range(45):
    print(bitList[i], end=" ")



