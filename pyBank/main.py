import os
import csv

#define file path
csvpath = os.path.join("Resources/budget_data.csv")

#open and read csv file 
with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader)
    
    #make a list of money and months
    #find total money by adding each component of the money list
    totalMoney = 0
    money_l = []
    months_l = []
    for row in csvreader:
        totalMoney = totalMoney + int(row[1])
        money_l.append(row[1])
        months_l.append(row[0])
    #find the total months
    totalMonths = len(months_l)
    
    #change money list from a list of strings to a list of integers
    for i in range(0, len(money_l)): 
        money_l[i] = int(money_l[i])
    
    #find the list of changes by subtracting the next value from the first value 
    change_l = []
    change = 0
    for num in range(0,(len(money_l)-1)):
        change = money_l[num + 1] - money_l[num]
        change_l.append(change)

    #find the min, max, and average of the changes
    gIncrease = max(change_l)
    gDecrease = min(change_l)
    avgChange = sum(change_l)/len(change_l)
    
    #find the dates that correspond to the max and min changes
    date1 = (change_l.index(gIncrease))+1
    date2 = (change_l.index(gDecrease))+1
    
    #find the dates that correspond to the max and min changes
    incDate = months_l[int(date1)]
    decDate = months_l[int(date2)]
    
    #print the results
    print(totalMonths)
    print(totalMoney)
    print(avgChange)
    print("Greatest increase in Profits: {} (${})".format(incDate,gIncrease))
    print("Greatest decrease in Profits: {} (${})".format(decDate,gDecrease))

 #create a text file and print the results   
newfilepath = "hwOutput.txt"
with open(newfilepath,"w") as txtfile:   
    txtfile.write("Financial Analysis")
    txtfile.write("\n")
    txtfile.write("--------------------") 
    txtfile.write("\n")
    txtfile.write("Total Months:{}".format(totalMonths))
    txtfile.write("\n")
    txtfile.write("Total Money: ${}".format(totalMoney))
    txtfile.write("\n")
    txtfile.write("Average Change: ${}".format(avgChange))
    txtfile.write("\n")
    txtfile.write(str("Greatest increase in Profits: {} (${})".format(incDate,gIncrease)))
    txtfile.write("\n")
    txtfile.write(str("Greatest decrease in Profits: {} (${})".format(decDate,gDecrease)))
