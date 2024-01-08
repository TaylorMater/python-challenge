####################################################################
####################################################################
# Riley Taylor
# 8 January 2024
# UT Data Analytics Bootcamp Module 3
####################################################################
####################################################################

#Instructions:
# In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
# You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:
#   The total number of votes cast
#   A complete list of candidates who received votes
#   The percentage of votes each candidate won
#   The total number of votes each candidate won
#   The winner of the election based on popular vote

# Your analysis should align with the following results:

# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.


###########################################################3

import os
import csv


#I assumed the data did not include duplicate votes


electionDataPath = os.path.join("Resources", "election_data.csv")

totalVotes = 0
#this dictionary is the workhorse. if candidate key is not found, add it with 1 vote as value
#if candidate key is found, incremenet the vote value
candidateVoteDict = {}

with open(electionDataPath, encoding="utf-8") as electionDataFile:
    csvreader = csv.reader(electionDataFile, delimiter=',')
    csvHeader = next(csvreader)

    for row in csvreader:
        #column 0 is ballot id, colum 1 is county, column 2 is candidate
        totalVotes += 1

        if (row[2] in candidateVoteDict):
            candidateVoteDict[row[2]] = candidateVoteDict[row[2]] + 1
        else:
            candidateVoteDict[row[2]] = 1


analysisFilePath = os.path.join("analysis", "pypoll_analysis.txt")
analysisStrings = []

analysisStrings.append("Election Results")
analysisStrings.append("-------------------------")
analysisStrings.append(f"Total Votes: {totalVotes}")
analysisStrings.append("-------------------------")

highestShare = 0
currentWinner = ""

for candidate in list(candidateVoteDict):
    percentageShare = candidateVoteDict[candidate]/totalVotes
    if (percentageShare > highestShare):
        highestShare = percentageShare
        currentWinner = candidate
    analysisStrings.append(f"{candidate}: {percentageShare:.3%} ({candidateVoteDict[candidate]})")

analysisStrings.append("-------------------------")
analysisStrings.append(f"Winner: {currentWinner}")
analysisStrings.append("-------------------------")


outputString = "\n".join(analysisStrings)

print(outputString)

with open(analysisFilePath, "w", encoding="utf-8") as analysisFile:
    analysisFile.write(outputString)