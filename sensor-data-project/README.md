#################### Note #######################
This project was taken and reuploaded from SFU's gitlab to github. The code I've written are in clean_data_filter.py, clean_data_filter.ipynb, clean_data_results.py, and clean_data_results.ipynb.
#################################################

General Description:
Our group chose to analyze if we could collect walking data and differentiate between subjects in our test group. To refine the question, we collected data for 3 different locations on the body: ankle, hand, and pocket. As a secondary problem we also tried to see if we could differentiate which part of the body the data was collected. The focus of our study is to analyze which data collection techniques and classification methods can best answer the question.

# Sensor Data Project
Project for CMPT 353.

# Required Libraries:
###### import sys
###### import pandas as pd
###### import numpy as np
###### import matplotlib.pyplot as plt
###### from scipy import stats
###### from pykalman import KalmanFilter
###### from datetime import datetime
###### from sklearn.model_selection import train_test_split
###### from sklearn.naive_bayes import GaussianNB
###### from sklearn.preprocessing import StandardScaler
###### from sklearn.neighbors import KNeighborsClassifier
###### from sklearn.tree import DecisionTreeClassifier
###### from sklearn.decomposition import PCA
###### from sklearn.svm import SVC
###### from sklearn.neural_network import MLPClassifier
###### from sklearn.pipeline import make_pipeline
###### from statsmodels.nonparametric.smoothers_lowess import lowess


# Order of Execution:
We need to run both the py and ipynb since, even though data was collected using the same app, it collects data differently on a Samsung device then an Apple device and the two programs clean data one for each.
1. ./clean_data_results.py
2. Run all clean_data_results.ipynb
3. Run all clean_data_filter.ipynb
4. ./clean_data_filter.py
5. Run all results_test.ipynb
