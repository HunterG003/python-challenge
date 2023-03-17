import os
import csv

greatestProfitIncrease = 0
greatestProfitIncreaseMonth = ""
greatestProfitDecrease = 0
greatestProfitDecreaseMonth = ""

csvpath = os.path.join('Resources', 'budget_data.csv')
writepath = os.path.join('analysis', 'financial_analysis.txt')

def findAverageChange(months, nums):

    numMonths = len(months)

    x1 = 0
    x2 = numMonths - 1

    y1 = nums[0]
    y2 = nums[numMonths-1]

    return round((y1 - y2) / (x1 - x2), 2)

with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile)

    header = next(csv_reader)

    months = []
    amounts = []

    netTotal = 0
    lastMonthCost = 0

    for row in csv_reader:
        cost = int(row[1])
        month = row[0]

        months.append(month)
        amounts.append(cost)

        change = cost - lastMonthCost

        if change > greatestProfitIncrease:
            greatestProfitIncrease = change
            greatestProfitIncreaseMonth = month
        elif change < greatestProfitDecrease:
            greatestProfitDecrease = change
            greatestProfitDecreaseMonth = month

        netTotal += int(cost)
        lastMonthCost = cost

    totalMonths = len(months)

    print("Financial Analysis\n")
    print("-----------------------------\n")
    print(f"Total Months: {totalMonths}")
    print(f"Total: ${netTotal}")
    print(f"Average change: ${findAverageChange(months, amounts)}")
    print(f"Greatest Increase in Profits: {greatestProfitIncreaseMonth} (${greatestProfitIncrease})")
    print(f"Greatest Decrease in Profits: {greatestProfitDecreaseMonth} (${greatestProfitDecrease})")