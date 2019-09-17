import os
import csv

csvpath = os.path.join("./Resources/budget_data.csv")
print(csvpath)

with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader)
    
    totalMoney = 0
    money_l = []
    months_l = []
    for row in csvreader:
        totalMoney = totalMoney + int(row[1])
        money_l.append(row[1])
        months_l.append(row[0])
    totalMonths = len(months_l)
    
    for i in range(0, len(money_l)): 
        money_l[i] = int(money_l[i])
    
    avgChange_l =[j - i for i, j in zip(money_l[:-1], money_l[1:])]
    
    gIncrease = max(avgChange_l)
    gDecrease = min(avgChange_l)
    avgChange = sum(avgChange_l)/len(avgChange_l)
    
    date1 = (avgChange_l.index(gIncrease))+1
    date2 = (avgChange_l.index(gDecrease))+1
    
    incDate = months_l[int(date1)]
    decDate = months_l[int(date2)]
    
    print(totalMonths)
    print(totalMoney)
    print(avgChange)
    print("Greatest increase in Profits: {} {}".format(incDate,gIncrease))
    print("Greatest decrease in Profits: {} {}".format(decDate,gDecrease))
    
newfilepath = "hwOutput.csv"
with open(newfilepath, mode="w", newline='') as csvfile2:
    csvwriter = csv.writer(csvfile2, delimiter=",")
    line1 = str(totalMonths)
    line2 = str(totalMoney)
    line3 = str(avgChange)
    line4 = str("Greatest increase in Profits: {} {}".format(incDate,gIncrease))
    line5 = str("Greatest decrease in Profits: {} {}".format(decDate,gDecrease))
    csvwriter.writerow(["Total Months:", line1])
    csvwriter.writerow(["Total Money:",  line2])
    csvwriter.writerow(["Average Change:",  line3])
    csvwriter.writerow(["Greatest Increase:",  line4])
    csvwriter.writerow(["Greatest Decrease:",  line5])