

import os
import csv

election1_csv = os.path.join("election_data_1.csv")
Election_Analysis = []
voters1 = []
candidates1 = []
candidate_list1 = []
Vestal = 0
Torres = 0
Seth = 0
Cordin = 0

with open (election1_csv, 'r') as csvfile:
    csv_reader1 = csv.reader(csvfile, delimiter=",")
    next(csv_reader1, None)
    for row in csv_reader1:
        voters1.append(row[0])
        candidates1.append(row[2])
        total_votes1 = len(voters1)
    for i in candidates1:
        if i not in candidate_list1:
            candidate_list1.append(i)
        elif i == 'Vestal':
            Vestal = Vestal + 1
        elif i == 'Torres':
            Torres = Torres + 1
        elif i == 'Seth':
            Seth = Seth + 1
        elif i == 'Cordin':
            Cordin = Cordin + 1
        Vestal_perc = Vestal/total_votes1
        Torres_perc = Torres/total_votes1
        Seth_perc = Seth/total_votes1    
        Cordin_perc = Cordin/total_votes1

election2_csv = os.path.join("election_data_2.csv")

voters2 = []
candidates2 = []
candidate_list2 = []

Khan = 0
Correy = 0
Li = 0
OTooley = 0
with open (election2_csv, 'r') as csvfile:
    csv_reader1 = csv.reader(csvfile, delimiter=",")
    next(csv_reader1, None)
    for row in csv_reader1:
        voters2.append(row[0])
        candidates2.append(row[2])
        total_votes2 = len(voters2)
    for i in candidates2:
        if i not in candidate_list2:
            candidate_list2.append(i)
        elif i == 'Khan':
            Khan = Khan + 1
        elif i == 'Correy':
            Correy = Correy + 1
        elif i == 'Li':
            Li = Li + 1
        elif i == "O'Tooley":
            OTooley = OTooley + 1
        Khan_perc = Khan/total_votes2
        Correy_perc = Correy/total_votes2
        Li_perc =Li/total_votes2    
        OTooley_perc = OTooley/total_votes2

total_votes = total_votes1 + total_votes2
candidate_list = candidate_list1 + candidate_list2
candidates = candidates1 + candidates2

Vestal_perc = Vestal/total_votes
Torres_perc = Torres/total_votes
Seth_perc = Seth/total_votes    
Cordin_perc = Cordin/total_votes
Khan_perc = Khan/total_votes
Correy_perc = Correy/total_votes
Li_perc = Li/total_votes    
OTooley_perc = OTooley/total_votes

Election_Analysis = [Vestal, Torres, Seth, Cordin, Khan, Correy, Li, OTooley]
Election_Perc = [Vestal_perc, Torres_perc, Seth_perc, Cordin_perc, Khan_perc, Correy_perc, Li_perc, OTooley_perc]
Winner = max(Election_Analysis)


'''

dictionary = dict(zip(candidate_list, Election_Analysis))
for keys, values in dictionary.items():
    print(keys, values)
    
'''


Election_Results = os.path.join("Election_Results.csv")
with open(Election_Results, 'w', newline="") as datafile:
    csvWriter = csv.writer(datafile)
    csvWriter.writerow(["Election Results"])
    csvWriter.writerow(["----------------------------"])
    csvWriter.writerow(["Total Votes: " + str(total_votes)])
    csvWriter.writerow(["----------------------------"])
    csvWriter.writerow(["Vestal: " + str(round(Vestal_perc*100, 0)) + "%" + " (" + str(Vestal) + ")"])
    csvWriter.writerow(["Torres: " + str(round(Torres_perc*100,0)) + "%" + " (" + str(Torres) + ")"])
    csvWriter.writerow(["Seth: " + str(round(Seth_perc*100, 0)) + "%" + " (" + str(Seth) + ")"])
    csvWriter.writerow(["Cordin: " + str(round(Cordin_perc*100, 0)) + "%" + " (" + str(Cordin) + ")"])
    csvWriter.writerow(["Khan: " + str(round(Khan_perc*100, 0)) + "%" + " (" + str(Khan) + ")"])
    csvWriter.writerow(["Correy: " + str(round(Correy_perc*100, 0)) + "%" + " (" +  str(Correy) + ")"])
    csvWriter.writerow(["Li: " + str(round(Li_perc*100, 0)) + "%" + " (" + str(Li) + ")"])
    csvWriter.writerow(["O'Tooley: " + str(round(OTooley_perc*100, 0)) + "%" + " (" + str(OTooley) + ")"])
    csvWriter.writerow(["----------------------------"])
    csvWriter.writerow(["Winner: " + str(candidate_list[Election_Analysis.index(max(Election_Analysis))])])
    csvWriter.writerow(["----------------------------"])

Election_Analysis = [Vestal_perc, Torres_perc, Seth_perc, Cordin_perc, Khan_perc, Correy_perc, Li_perc, OTooley_perc]
Winner = max(Election_Analysis)

print("Election Results")
print("----------------------------")
print("Total Votes: " + str(total_votes))
print("----------------------------")
print("Vestal: " + str(round(Vestal_perc*100, 0)) + "% " + "(" + str(Vestal) + ")")
print("Torres: " + str(round(Torres_perc*100, 0)) + "% " + "(" + str(Torres) + ")")

print("Seth: " + str(round(Seth_perc*100, 0)) + "% " + "(" + str(Seth) + ")")
print("Cordin: " + str(round(Cordin_perc*100, 0)) + "% " + "(" + str(Cordin) + ")")
print("Khan: " + str(round(Khan_perc*100, 0)) + "% " + "(" + str(Khan) + ")")
print("Correy: " + str(round(Correy_perc*100, 0)) + "% " + "(" + str(Correy) + ")")
print("Li: " + str(round(Li_perc*100, 0)) + "% " + "(" + str(Li) + ")")
print("O'Tooley: " + str(round(OTooley_perc*100, 0)) + "% " + " (" + str(OTooley) + ")")
print("----------------------------")
print("Winner: " + str(candidate_list[Election_Analysis.index(max(Election_Analysis))]))
print("----------------------------")






      


