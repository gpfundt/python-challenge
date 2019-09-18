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
    
    change_l = []
    change = 0
    for num in range(0,(len(money_l)-1)):
        change = money_l[num + 1] - money_l[num]
        change_l.append(change)

    gIncrease = max(change_l)
    gDecrease = min(change_l)
    avgChange = sum(change_l)/len(change_l)
    
    date1 = (change_l.index(gIncrease))+1
    date2 = (change_l.index(gDecrease))+1
    
    incDate = months_l[int(date1)]
    decDate = months_l[int(date2)]
    
    print(totalMonths)
    print(totalMoney)
    print(avgChange)
    print("Greatest increase in Profits: {} {}".format(incDate,gIncrease))
    print("Greatest decrease in Profits: {} {}".format(decDate,gDecrease))
    
newfilepath = "hwOutput.txt"
with open(newfilepath,"w") as txtfile:
    #line1 = str(totalMonths)
    #line2 = str(totalMoney)
    #line3 = str(avgChange)
    
    txtfile.write("Total Months:{}".format(totalMonths))
    txtfile.write("\n")
    txtfile.write("Total Money:{}".format(totalMoney))
    txtfile.write("\n")
    txtfile.write("Average Change: {}".format(avgChange))
    txtfile.write("\n")
    txtfile.write(str("Greatest increase in Profits: {} {}".format(incDate,gIncrease)))
    txtfile.write("\n")
    txtfile.write(str("Greatest decrease in Profits: {} {}".format(decDate,gDecrease)))
