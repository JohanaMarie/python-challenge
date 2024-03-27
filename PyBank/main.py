# IMPORTS
import csv
import os

# CONSTANTS
CSV_PATH = os.path.join('Resources', 'budget_data.csv')
OUTPUT_PATH = os.path.join('Analysis', 'financial_analysis.txt')

# VARIABLES
total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
profit_loss_changes = []
months = []

# CODE/PROCEDURE
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Profit/Losses total number of months
with open(CSV_PATH) as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    for row in csv_reader:
        # total months
        total_months += 1

        # total Profit/Losses
        total_profit_loss += int(row[1])

        # profit/loss w/ months
        profit_loss = int(row[1])
        profit_loss_changes.append(profit_loss - previous_profit_loss)
        previous_profit_loss = profit_loss
        months.append(row[0])

# average change in Profit/Losses
average_change = sum(profit_loss_changes[1:]) / (total_months - 1)

# greatest increase/decrease in profits
greatest_increase = max(profit_loss_changes)
greatest_increase_month = months[profit_loss_changes.index(greatest_increase)]
greatest_decrease = min(profit_loss_changes)
greatest_decrease_month = months[profit_loss_changes.index(greatest_decrease)]

# print to git bash/terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# export to analysis file
with open(OUTPUT_PATH, 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${total_profit_loss}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")

print("Results exported to 'financial_analysis.txt'")