from os import popen
import sys
import numpy as np
import pandas as pd
from datetime import date, datetime
import os.path
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import subprocess

hard_test_accuracy = False
iteration = '2'

eval_results = pd.read_csv('evaluation/model_eval.csv', parse_dates=['time_stamp'], dayfirst=True)

last_run = eval_results['time_stamp'].max()

Accurracy_logs = eval_results[eval_results['metric']=='accuracy']

last_accuracy = Accurracy_logs[Accurracy_logs['time_stamp']==last_run]['accuracy'].values[0]
all_other_accuracy = Accurracy_logs[Accurracy_logs['time_stamp']!=last_run]['accuracy'].values

print(last_accuracy)
print(all_other_accuracy)

hard_test_accuracy = last_accuracy <= np.mean(all_other_accuracy)

print('\n.. Hard Test ..')
print('Accuracy drift: ', hard_test_accuracy)

if(hard_test_accuracy):
    print('Creating model for data set number: ' + iteration + '\n')
    cmdLine = 'python train.py ' + iteration
    subprocess.Popen(cmdLine)

