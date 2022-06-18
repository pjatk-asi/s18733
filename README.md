# Table of contents #
1. [General](#general)
2. [Data](#data)
2. [Archtecture](#architecture)
3. [Installation](#installation)
4. [About author](#about-author)


## General ##

The main purpose of this app is to predict stroke based on lifestyle. Initially, we will use real input data to train the model and check whether it will adequately predict the results of the test data. The next step will be to reverse the initial results, find drift and retrain the model on new data.

## Data ##

Our data is a set of basic information about a given person, such as age, gender. The next data concern the lifestyle, whether the person smokes, what kind of job they have. There is also medical data such as average glucose level. What interests us the most is the stroke column, which indicates whether a person with a given lifestyle suffered a stroke or not.


## Architecture ## 


## Installation ##
If you have installed conda all you need to do is:
1. Create environment:
	$ conda env create -f environment.yml
2. Activate enviroment:
	$ conda activate ASI

## About author ##
Bartosz Kami?ski - S18733