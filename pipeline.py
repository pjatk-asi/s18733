import subprocess
from evaluate import evaluate_fun
from read import read_fun
from train import train_fun
from detect_model_drift import detectDrift_fun

for x in range(1, 3):
    iteration = str(x)
    print('Start iteration for dataset number: ' + iteration)
    read_fun(iteration)
    evaluate_fun(iteration)
    detectDrift_fun(iteration)