# IMPORTS
import csv
import os

# CONSTANTS
CSV_PATH = os.path.join('Resources', 'election_data.csv')
OUTPUT_PATH = os.path.join('Analysis', 'election_analysis.txt')

# VARIABLES
total_votes = 0
candidate_votes = {}

# CODE/PROCEDURE
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# total votes
with open(CSV_PATH) as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    for row in csv_reader:
        total_votes += 1
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# winner
winner = max(candidate_votes, key=candidate_votes.get)

# print to git bash/terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# export to analysis file
with open(OUTPUT_PATH, 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        output_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")

print("Analysis results exported to 'election_analysis.txt'")
