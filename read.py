import pandas as pd
import sys

def read_fun(iteration):
    print('Read function for data set number: ' + iteration)
    df = pd.read_csv('data' + iteration +'/dataset-init.csv')

    df.to_csv('data' + iteration +'/dataset-train.csv', index=False)