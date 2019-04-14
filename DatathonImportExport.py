""" The purpose of this file is to import existing mosquito trapping data that has been standardized
to compute relative abundance of mosquitoes by county and month, then aggregate each month's data so as to sum
across all trap types.  The finalized data set should not have duplicate rows for each month and should reflect the
expected relative abundance of mosquitoes in that county (aegypti, albopictus) in the last two columns, respectively.
This finalized data set is stored in a new array and exported to a new .csv file.
"""


# import packages numpy and csv
import numpy as np
import csv


def main():

# import mosquito data as array of strings, store as totalData
    abs_file_path = "C:/Users/Richard/Desktop/stanford_blueprint_datathon_2019_data_2.csv" # give exact path name for mosquito data to import
    with open(abs_file_path, newline='') as csvfile: # read in mosquito data and store in totalData
        totalData = list(csv.reader(csvfile))





    revisedData =[] # initiate array for storing filtered (revised) data


    for i in range(len(totalData)): # begin loop indexed by the number of rows in the totalData array
        tempRow = []
        for x in range(len(totalData[i])):
            if totalData[i][x] == "low":
                tempRow.append('1')
            elif totalData[i][x] == "medium":
                tempRow.append('2')
            elif totalData[i][x] == "high":
                tempRow.append('3')
            else:
                tempRow.append(totalData[i][x])

        revisedData.append(tempRow)



    # export newly compiled data to a new .csv file
    myFile = open('/Users/Richard/Desktop/revised_Datathon.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(revisedData)

main()