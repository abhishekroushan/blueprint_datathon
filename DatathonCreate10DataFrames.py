import numpy as np
import csv
import pandas as pd
import sys


def main():


    abs_file_path = "C:/Users/Richard/Desktop/revised_Datathon/revised_Datathon.csv" # give exact path name for mosquito data to import

    data = pd.read_csv(abs_file_path)


    labels = ['chlamydia', 'gential_warts', 'gonorrhea', 'herpes', 'hpv', 'other_std', 'parasitic', 'std_screen', 'syphilis', 'trich']

    for u in range(10):

        tempData = data.drop(data.columns[69:79], axis=1)






        df = data[labels[u]].to_frame()




        tempData = pd.concat([tempData, df], axis=1)



        #filtered_df = tempData[tempData[labels[u]].notna()]
        filtered_df = tempData.dropna()
        #print(tempData.values[11,:])

        #print(tempData[labels[u]].notna())
        #print(labels[u])
        print(filtered_df.shape)
        tempData = filtered_df.values.tolist()






               # export newly compiled data to a new .csv file
        filename = '/Users/Richard/Desktop/Datathon_dataset'+str(u)+'.csv'
        myFile = open(filename, 'w')
        with myFile:
            writer = csv.writer(myFile)
            writer.writerows(tempData)





main()