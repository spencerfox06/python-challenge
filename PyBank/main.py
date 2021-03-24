import os
import csv

# create variable and point to data source
pybank_csv = os.path.join('Resources', 'budget_data.csv')

total_months = 0
prev_net = 0
total_net = 0
Great_Inc = ['', 0]
Great_Dec = ['', 100000000]

Change_List = []

# open and read csv file
with open(pybank_csv, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    
    column_names = next(csv_reader)
    first_row = next(csv_reader)

    total_net += int(first_row[1])
    prev_net += int(first_row[1])
    total_months += 1

    for row in (csv_reader):

        total_months += 1

        total_net += int(row[1])

        Monthly_Change = int(row[1]) - prev_net
        prev_net = int(row[1])
        Change_List += [Monthly_Change]
        

        Avg_Change = sum(Change_List) / len(Change_List)
        
        if Monthly_Change > Great_Inc[1]:
            Great_Inc[0] = row[0]
            Great_Inc[1] = Monthly_Change

        if Monthly_Change < Great_Dec[1]:
            Great_Dec[0] = row[0]
            Great_Dec[1] = Monthly_Change
        
        #Great_Inc = "${:,.2f}".format((max(Change_List)))
        #Great_Inc_Month = (row[0])
        #Great_Dec = "${:,.2f}".format((min((Change_List))))
        #Great_Dec_Month = (row[0])

        #print(Monthly_Change)
        #print(Change_List)
        #print(Great_Inc))
        #print(Great_Dec)

    Output = (
    '\n'
    'Financial Analysis\n'
    '------------------\n'
    f'Total Months: {total_months}\n'
    f'Total Revenue: ${total_net:.0f}\n'
    f'Average Change: ${Avg_Change:.2f}\n'
    f'Greatest Increase in Profits: {Great_Inc[0]} $({Great_Inc[1]})\n'
    f'Greatest Decrease in Profits: {Great_Dec[0]} $({Great_Dec[1]})\n'

    )

    print(Output)

with open('Analysis.txt', 'w') as Txtfile:
    Txtfile.write(Output)

#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)       


# Wrestling Activity
#------------------------
#def Profit_Loss_Data(row):
    #print(row)

    #Months = row[0]
    #Profit_Loss = int(row[1])

    #total_profit_loss = Profit_Loss


    # AskBCS Input
#------------------

#with open(pybank_csv) as financial_data:
   #reader = csv.reader(financial_data)

# Read the header row
#header = next(csv_reader)

# Extract first row to avoid appending to net_change_list
#first_row = next(csv_reader)
#total_months += 1
#total_net += int(first_row[1])
#prev_net = int(first_row[1])
#---------------------------------
