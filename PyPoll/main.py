import os
import csv

# create variable and point to data source
pypoll_csv = os.path.join('Resources', 'election_data.csv')

# open and read csv file
with open(pypoll_csv, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

    first_row = next(csv_reader)
    Candidate_Selection = 0
    Khan_Count = 0
    Correy_Count = 0
    Li_Count = 0
    OTooley_Count = 0
        
    for row in csv_reader:
        
        Candidate_Selection += 1

        if row[2] == 'Khan':
            Khan_Count += 1
        elif row[2] == 'Correy':
            Correy_Count += 1
        elif row[2] == 'Li':
            Li_Count += 1
        else:
            OTooley_Count += + 1

Khan_Percent = "{:00.3%}".format(Khan_Count / Candidate_Selection)
Correy_Percent = "{:00.3%}".format(Correy_Count / Candidate_Selection)
Li_Percent = "{:00.3%}".format(Li_Count / Candidate_Selection)
OTooley_Percent = "{:00.3%}".format(OTooley_Count / Candidate_Selection)

Output = (
    '\n'
    'Election Results\n'
    '------------------\n'
    f'Total Votes: {Candidate_Selection}\n'
    '------------------\n'
    f'Khan: {Khan_Percent} ({Khan_Count})\n'
    f'Correy: {Correy_Percent} ({Correy_Count})\n'
    f'Li: {Li_Percent} ({Li_Count})\n'
    f'OTooley: {OTooley_Percent} ({OTooley_Count})\n'
    '------------------\n'
    'Winner: Khan\n'
    '------------------\n'

    )

print(Output)

with open('Analysis.txt', 'w') as Txtfile:
    Txtfile.write(Output)

#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   ```