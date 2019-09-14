import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")
print(csvpath)
with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csvheader = next(csvreader)
    
    totalMoney = 0
    money_l = []
    for row in csvreader:
        totalMoney = totalMoney + int(row[1])
        money_l.append(row[1])
    totalMonths = len(money_l)
    print(totalMonths)
    print(totalMoney)
    
    for i in range(0,len(money_l)):
        money_l[i] = int(money_l[i])
    avgChange = statistics.stdev(money_l)
    print(avgChange)


