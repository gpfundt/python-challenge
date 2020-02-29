import os
import csv

#create path to read election_data csv in Resources
csvpath = os.path.join("Resources", "election_data.csv")
 
#read csv file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader)
    
    #separate column of votes from csv file
    votes_l = []
    for row in csvreader:
        votes_l.append(row[2])
    totalVotes = len(votes_l)
    
    #find each candidate that recieved votes
    candidates_l = []
    for candidate in votes_l:
        if candidate not in candidates_l:
            candidates_l.append(candidate)
    
    #find each candidate
    candidate_1 = candidates_l[0]
    candidate_2 = candidates_l[1]
    candidate_3 = candidates_l[2]
    candidate_4 = candidates_l[3]
    
    #1st candidate votes and percent
    votes_c1 = votes_l.count(candidate_1)
    percent_c1 = round((votes_c1/totalVotes * 100),2)
    #2nd candidate votes and percent
    votes_c2 = votes_l.count(candidate_2)
    percent_c2 = round((votes_c2/totalVotes * 100),2)
    #3rd candidate votes and percent
    votes_c3 = votes_l.count(candidate_3)
    percent_c3 = round((votes_c3/totalVotes * 100),2)
    #4th candidate votes and percent
    votes_c4 = votes_l.count(candidate_4)
    percent_c4 = round((votes_c4/totalVotes * 100),2)
    
    #find winer based on largest amount of votes
    winner_Amt = max([votes_c1,votes_c2,votes_c3,votes_c4])
    
    #find winners name that corresponds to those votes
    if winner_Amt == votes_c1:
        winner = candidate_1
    elif winner_Amt == votes_c2:
        winner = candidate_2
    elif winner_Amt == votes_c3:
        winner = candidate_3
    elif winner_Amt == votes_c4:
        winner = candidate_4

    #print results
    print("Total Votes: {}".format(totalVotes))
    print("{}: {}% ({})".format(candidate_1,percent_c1,votes_c1))
    print("{}: {}% ({})".format(candidate_2,percent_c2,votes_c2))
    print("{}: {}% ({})".format(candidate_3,percent_c3,votes_c3))
    print("{}: {}% ({})".format(candidate_4,percent_c4,votes_c4))
    print("Winner is {}".format(winner))
 
    #output a txt file with results
    newfilepath = "hwOutput.txt"
    with open(newfilepath,"w") as txtfile:   
        txtfile.write("Election Results")
        txtfile.write("\n")
        txtfile.write("--------------------") 
        txtfile.write("\n")
        txtfile.write("Total Votes: {}".format(totalVotes))
        txtfile.write("\n")
        txtfile.write("--------------------") 
        txtfile.write("\n")
        txtfile.write("{}: {}% ({})".format(candidate_1,percent_c1,votes_c1))
        txtfile.write("\n")
        txtfile.write("{}: {}% ({})".format(candidate_2,percent_c2,votes_c2))
        txtfile.write("\n")
        txtfile.write("{}: {}% ({})".format(candidate_3,percent_c3,votes_c3))
        txtfile.write("\n")
        txtfile.write("{}: {}% ({})".format(candidate_4,percent_c4,votes_c4))
        txtfile.write("\n")
        txtfile.write("--------------------")
        txtfile.write("\n")
        txtfile.write("Winner is {}".format(winner))
        txtfile.write("\n")
        txtfile.write("--------------------") 