import os
import numpy as np
import pandas as pd

def load_st_dataset(dataset):
    #output B, N, D
    if dataset == 'PEMSD7(M)':
        data_path = os.path.join('./data/PEMS07(M)/V_228.csv')
        data = np.array(pd.read_csv(data_path,header=None)) 
    elif dataset == 'Melb':
        data_path = os.path.join('./data/Melb.h5')
        # speed = pd.read_hdf(data_path, key = 'speed', mode='r')
        data = pd.read_hdf(data_path, key='flow', mode='r')
        # data = np.stack((flow, speed), axis=-1)
    else:
        raise ValueError
    if len(data.shape) == 2:
        data = np.expand_dims(data, axis=-1)
    print('Load %s Dataset shaped: ' % dataset, data.shape, data.max(), data.min(), data.mean(), np.median(data))
    return data

