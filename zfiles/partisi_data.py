# -*- coding: utf-8 -*-

import h5py as h5
import numpy as np
from sklearn.model_selection import KFold,StratifiedShuffleSplit

# %% Atribut dan target

f = h5.File('cwt181morl_fea.mat','r')
data = f.get('data_energy')
xdata = np.array(data)
xdata = np.transpose(data)

tar1, tar2, tar3 = [0]*21, [1]*12, [2]*35
ydata = tar1+tar2+tar3
ydata = np.ravel(ydata)

# %% Partisi data dengan Cross Validation


#for i in range(5):
for i in range(1):    
    nfo = KFold(n_splits=3)
    
    tridx, teidx = [],[]
    for train_index, test_index in nfo.split(xdata,ydata):
        tridx.append(train_index)
        teidx.append(test_index)
        
        #print(train_index,test_index)
        print(len(train_index),':',len(test_index))
    
    np.save('cvfolds/2kfcvL'+str(i+1)+'.npy',tridx)
    np.save('cvfolds/2kfcvU'+str(i+1)+'.npy',teidx)
'''    
for i in range(1):
    skf = StratifiedShuffleSplit(n_splits=6, test_size=0.3, train_size=0.7)

    tridx, teidx = [],[]
    for train_index, test_index in skf.split(xdata, ydata):
        tridx.append(train_index)
        teidx.append(test_index)
        
        print(len(train_index),':',len(test_index))
    
    np.save('cvfolds/shspcvL'+str(i+1)+'.npy',tridx)
    np.save('cvfolds/shspcvU'+str(i+1)+'.npy',teidx)    
'''