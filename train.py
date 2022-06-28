import sys
import pandas as pd
import numpy as np
from sklearn import preprocessing
from urllib.parse import urlparse
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from pycaret.classification import *

def train_fun(iteration):
    print('Train function for data set number: ' + iteration)

    dataset = pd.read_csv('data' + iteration + '/dataset-train.csv')

    data = dataset.sample(frac=0.8, random_state=322)

    data.reset_index(drop=True, inplace=True)

    data_unseen = dataset.drop(data.index)

    data_unseen.reset_index(drop=True, inplace=True)

    data_unseen.to_csv('data' + iteration + '/dataset-test.csv', index=False)

    exp1 = setup(data=data, target='stroke', session_id=121, log_experiment = True, experiment_name="stroke prediction", silent=True)

    best = compare_models()

    evaluate_model(best)

    final = finalize_model(best)

    predict_model(final)

    save_model(final, model_name='model/model')
