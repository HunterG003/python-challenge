import os
import csv

# Variables
numVotes = 0
candidates = {}
winner = ''
highestVotes = 0

csvpath = os.path.join('Resources', 'election_data.csv')

# Gets percentage from total votes
def calculatePercentVote(numVotes, numTotalVotes):
    return round(numVotes / numTotalVotes * 100, 3)

# Columns: Ballot ID, County, Candidate

with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile)
    header = next(csv_reader)

    for row in csv_reader:
        if row[2] in candidates:
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

        numVotes += 1

lines = []

# Creates lines
lines.append("Election Results")
lines.append("----------------------")
lines.append(f"Total Votes: {numVotes}")
lines.append("----------------------")

# Goes through candidates and  calculate
for candidate, votes in candidates.items():
    percentage = calculatePercentVote(votes, numVotes)
    lines.append(f"{candidate}: {percentage}% ({votes})")

    if votes > highestVotes:
        highestVotes = votes
        winner = candidate

lines.append("----------------------")
lines.append(f"Winner: {winner}")
lines.append("----------------------")


# Print Results
for line in lines:
    print(line)

# Write Results
writeto = os.path.join('analysis', 'Election_Results.txt')

with open(writeto, 'w') as writefile:
    for line in lines:
        writefile.write(line + '\n')