import numpy as np
import csv
import pandas as pd
import sys
import seaborn as sns

def main():


    abs_file_path = "C:/Users/Richard/Desktop/10DataSets/datathon_dataset_trich.csv" # give exact path name for mosquito data to import

    data = pd.read_csv(abs_file_path)

    sampleData = data.sample(frac=0.005, random_state=1)

    #predictorLabels = data.reset_index()
    predictorLabels = list(data)
    predictorLabels = predictorLabels[5:-2]
    print(predictorLabels)

    sampleData['trich'].apply(np.log)



    pp = sns.pairplot(data=sampleData,
                      y_vars=['trich'],
                      x_vars=predictorLabels, kind='reg')


    pp.savefig('trich.png')







main()