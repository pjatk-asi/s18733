from datetime import date, datetime
import os.path
import sys
import pandas as pd
import pickle
import logging
from pycaret.classification import *
from sklearn.metrics import accuracy_score


data_file_name = 'data2/dataset-init.csv'

test_data = pd.read_csv(data_file_name)
model = load_model("model/model")

predictions = predict_model(model, data = test_data)

accuracy = accuracy_score(predictions['stroke'], predictions['Label'])

print('Accuracy on test data: ', accuracy)

eval_df = pd.DataFrame()

now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

eval_df = eval_df.append({'time_stamp':now, 'version': '1.0', 'batch': 2, 'metric': 'accuracy', 'accuracy': accuracy}, ignore_index=True)

evaluation_file_name = 'evaluation/model_eval.csv'

if os.path.isfile(evaluation_file_name):
    eval_df.to_csv('evaluation/model_eval.csv', mode='a', index=False, header=False)
else:
    eval_df.to_csv('evaluation/model_eval.csv', index=False)