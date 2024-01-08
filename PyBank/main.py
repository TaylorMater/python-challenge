####################################################################
####################################################################
# Riley Taylor
# 8 January 2024
# UT Data Analytics Bootcamp Module 3
####################################################################
####################################################################

import os
import csv

# Your task is to create a Python script that analyzes the records to calculate each of the following values:
#   The total number of months included in the dataset
#   The net total amount of "Profit/Losses" over the entire period
#   The changes in "Profit/Losses" over the entire period, and then the average of those changes
#   The greatest increase in profits (date and amount) over the entire period
#   The greatest decrease in profits (date and amount) over the entire period

# Your analysis should align with the following results:

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)

#pandas was not allowed for this assignment
#variables to hold the above requirements

#counts months we have iterated through in the csv
totalMonths = 0
#a net sum of the profit/loss column as we iterate through the csv
netTotalProfitLoss = 0
#in theory not needed because you could recompute a mean as you go, and just use the totalMonths variable as a counter, but probably useful to have this for debugging purposes
profitLossChanges = []
#to compute the changes
lastProfitLoss = 0
#aveageChange set to 0 in the event that no change occurs/too small of a data set so that code doesn't stumble
averageChange = 0
#first element contains running max increase, second contains the string of the date (essentially using this as a struct)
maxIncreaseInfo = []
#first element contains running max decrease, second contains the string of the date (essentially using this as a struct)
maxLossInfo = []

budget_data_csv_path = os.path.join("Resources", "budget_data.csv")

with open(budget_data_csv_path, encoding="utf-8") as budget_csv:
    csvreader = csv.reader(budget_csv, delimiter=",")

    #handle the header row:
    csvHeader = next(csvreader)

    #iterate through csv
    for row in csvreader:
        totalMonths += 1
        netTotalProfitLoss += int(row[1])

        #calculate/save/check the change if we have space to calculate
        if (totalMonths > 1):
            currentChange = int(row[1]) - lastProfitLoss
            profitLossChanges.append(currentChange)
            #check if maxIncreaseInfo is populated or not
            if (maxIncreaseInfo):
                if (currentChange > maxIncreaseInfo[0]):
                    maxIncreaseInfo[0] = currentChange
                    maxIncreaseInfo[1] = row[0]
            else:
                maxIncreaseInfo.append(currentChange)
                maxIncreaseInfo.append(row[0])
            #check if maxLossInfo is populated or not
            if (maxLossInfo):
                if (currentChange < maxLossInfo[0]):
                    maxLossInfo[0] = currentChange
                    maxLossInfo[1] = row[0]
            else:
                maxLossInfo.append(currentChange)
                maxLossInfo.append(row[0])

        #save the profit loss for the next row to reference
        lastProfitLoss = int(row[1])





analysisFilePath = os.path.join("analysis","pybank_analysis.txt")
analysisStrings = []

#formatting the string to write to an analysis file
    #it makes more sense to split this into a separate file/function, but we will not focus too heavily on this
try:

    averageChange = sum(profitLossChanges)/len(profitLossChanges)

    analysisStrings.append("Financial Analysis")
    analysisStrings.append("----------------------------")
    analysisStrings.append(f"Total Months: {totalMonths}")
    analysisStrings.append(f"Total: ${netTotalProfitLoss}")
    analysisStrings.append(f"Average Change: ${averageChange:.2f}")
    analysisStrings.append(f"Greatest Increase in Profits: {maxIncreaseInfo[1]} (${maxIncreaseInfo[0]})")
    analysisStrings.append(f"Greatest Decrease in Profits: {maxLossInfo[1]} (${maxLossInfo[0]})")
    
except:
    print("Ill-defined data. Check that there is data. Defaults might be used if no data present. ")

#to write to the output file
with open(analysisFilePath, "w", encoding="utf-8") as analysisFile:
    analysisFile.write("\n".join(analysisStrings))

#purely to tell the grader 
print("If no error has been printed, then the analysis has been written to the \"analysis\\pybank_analysis.txt\" file. If the file is empty, then the data was not handled/formatted properly.")
