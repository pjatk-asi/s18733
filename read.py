import pandas as pd
import sys

#iteration = str(sys.argv[1])
iteration = '2'

df = pd.read_csv('data1/dataset-init.csv')

df.to_csv('data1/dataset-train.csv', index=False)