# IMPORTS
import csv
import os

# CONSTANTS
CSV_PATH = os.path.join('Resources', 'budget_data.csv')

# CODE/PROCEDURE
os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(CSV_PATH) as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    for row in csv_reader:
        print(row, type(row))














# #The total number of months included in the dataset
# total_months =
# #The net total amount of "Profit/Losses" over the entire period
# total =
# #The changes in "Profit/Losses" over the entire period, and then the average of those changes
# average_change =
# #The greatest increase in profits (date and amount) over the entire period
# greatest_increase = 
# #The greatest decrease in profits (date and amount) over the entire period
# greatest_decrease =