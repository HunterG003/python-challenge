import os
import csv

greatestProfitIncrease = 0
greatestProfitDecrease = 0

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile)

    header = next(csv_reader)

    months = []
    amounts = []

    netTotal = 0

    for row in csv_reader:
        cost = row[1]
        month = row[0]

        months.append(month)
        amounts.append(cost)

        netTotal += int(cost)

    totalMonths = len(months)

    print("Finanical Analysis\n")
    print("-----------------------------\n")
    print(f"Total Months: {totalMonths}")
    print(f"Total: ${netTotal}")
    print(f"Average change: $")
    print(f"Greatest Increase in Profits: ")
    print(f"Greatest Decrease in Profits: ")