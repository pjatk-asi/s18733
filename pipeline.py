import subprocess

for x in range(1, 5):
    iteration = str(x)
    print('\n' + "Iterate data set number: " + str(x) + '\n')

    print('Evalutaion model for data set number: ' + iteration + '\n')
    cmdLine = 'python evaluate.py ' + iteration
    p = subprocess.Popen(cmdLine)
    p_status = p.wait()

    print('Detect drift for data set number: ' + iteration + '\n')
    cmdLine = 'python detect_model_drift.py ' + iteration
    p = subprocess.Popen(cmdLine)
    p_status = p.wait()


    print('Create training data set for data set number: ' + iteration + '\n')
    cmdLine = 'python read.py ' + iteration
    #p = subprocess.Popen(cmdLine, stdout=subprocess.PIPE, shell=True)
    #p.wait()


    print('Creating model for data set number: ' + iteration + '\n')
    cmdLine = 'python train.py ' + iteration
    #p = subprocess.Popen(cmdLine, stdout=subprocess.PIPE, shell=True)
    #p.wait()

    sec = input('Click enter \n')