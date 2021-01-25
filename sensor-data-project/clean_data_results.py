import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.nonparametric.smoothers_lowess import lowess
import glob

def to_float(x):
    return float(x)

def get_csv(filename):
    """
    Reads the csv file and clean up the data to include the nessesary columns.
    """
    column_name = ['time', 'x_accel', 'y_accel', 'z_accel', 'total_accel']
    raw_data = pd.read_csv(filename, names=column_name, header=None) 
    raw_data = raw_data.drop(0) 
    raw_data['time'] = raw_data['time'].apply(to_float)
    raw_data['x_accel'] = raw_data['x_accel'].apply(to_float)
    raw_data['y_accel'] = raw_data['y_accel'].apply(to_float)
    raw_data['z_accel'] = raw_data['z_accel'].apply(to_float)
    
    return raw_data

def extract_features(raw_data):
    """
    Prepare and extract features from the data to be used in prediction models.
    Current features: mean, std.
    """
    ret = raw_data[raw_data['time'] < 30]
    mean = ret.mean().tolist()
    std = ret.std().tolist()
    
    return mean, std

def process_data(input_file_dir, output_dir, tester_num):
    """
    Takes the input directory containing a tester's data and their id number
    and outputs a csv file containing the mean and std of their data.
    """
    frames_mean = []
    frames_std = []
    fileNames = sorted(glob.glob(input_file_dir + '*'))
    for name in fileNames:
      raw_data = get_csv(name)
      mean, std = extract_features(raw_data)
      frames_mean.append(mean)
      frames_std.append(std)

    output_file = output_dir + 'p' + tester_num
    col = ['time', 'x_accel', 'y_accel', 'z_accel']

    # Output mean to csv file.
    results_mean = pd.DataFrame(frames_mean, columns=col)
    results_mean['tester'] = tester_num
    results_mean.to_csv(output_file + "-mean.csv")
    # Output std to csv file.
    results_std = pd.DataFrame(frames_std, columns=col)
    results_std['tester'] = tester_num
    results_std.to_csv(output_file + "-std.csv") 
    
def main():
    # get output for tester 1
    output_loc = 'data/processed/'
    inName = "data/raw/1/"
    tester_num = "1"
    process_data(inName, output_loc, tester_num)

    #get output for tester 2
    inName = "data/raw/2/"
    tester_num = "2"
    process_data(inName, output_loc, tester_num)

if __name__ == "__main__":
    main()
