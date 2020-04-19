# -*- coding: utf-8 -*-

import h5py as h5
import numpy as np
from sklearn.externals import joblib
from sklearn.metrics import accuracy_score, confusion_matrix

# %% Baca data

# DWT features (n_feature = 46)
fdwt = h5.File('dwt7db2_fea.mat','r')
#fdwt = h5.File('dwt7db2unpre_fea.mat','r')

data = fdwt.get('feas')
xdata = np.array(data)
xdata = np.transpose(data)

# %% Labelling

tar1, tar2, tar3 = [0]*21, [1]*12, [2]*35
ydata = tar1+tar2+tar3
ydata = np.ravel(ydata)

# %% Mulai uji model SVM

'''
# SVM yang diuji dengan features yang direduksi oleh autoencoder
#for i in range(5):
for i in range(1):    
    cvfolds = np.load('cvfolds/kfcvU'+str(i+1)+'.npy')
    #cvfolds = np.load('cvfolds/shspcvU'+str(i+1)+'.npy')
    print('cvfolds/cvfoldsU'+str(i+1)+'.npy')
    scores,f1s = [],[]
    for j in range(len(cvfolds)):
        # Reduced features (n_feature = 5)
        #xdata = np.load('encoded/atncdr_aVII5_morl_kfcv'+str(i+1)+'_'+str(j)+'.npy')
        #xdata = np.load('encoded/atncdr_aVII5_morl_shspcv'+str(i+1)+'_'+str(j)+'.npy')
        # Reduced features (n_feature = 10)
        #xdata = np.load('encoded/atncdr_bVII10_morl_kfcv'+str(i+1)+'_'+str(j)+'.npy')
        #xdata = np.load('encoded/atncdr_bVII10_morl_shspcv'+str(i+1)+'_'+str(j)+'.npy')
        # Reduced features (n_feature = 15)
        #xdata = np.load('encoded/atncdr_cVII15_morl_kfcv'+str(i+1)+'_'+str(j)+'.npy')
        #xdata = np.load('encoded/atncdr_cVII15_morl_shspcv'+str(i+1)+'_'+str(j)+'.npy')
        # Reduced features (n_feature = 20)
        xdata = np.load('encoded/atncdr_dVII20_morl_kfcv'+str(i+1)+'_'+str(j)+'.npy')
        #xdata = np.load('encoded/atncdr_dVII20_morl_shspcv'+str(i+1)+'_'+str(j)+'.npy')
        
        #clf = joblib.load('model/svmatn5_VII_morl_kfcvL'+str(i+1)+'_'+str(j)+'.joblib')
        #clf = joblib.load('model/svmatn5_VII_morl_shspcvL'+str(i+1)+'_'+str(j)+'.joblib')

        #clf = joblib.load('model/svmatn10_VII_morl_kfcvL'+str(i+1)+'_'+str(j)+'.joblib')
        #clf = joblib.load('model/svmatn10_VII_morl_shspcvL'+str(i+1)+'_'+str(j)+'.joblib')
        
        #clf = joblib.load('model/svmatn15_VII_morl_kfcvL'+str(i+1)+'_'+str(j)+'.joblib')
        #clf = joblib.load('model/svmatn15_VII_morl_shspcvL'+str(i+1)+'_'+str(j)+'.joblib')
        
        clf = joblib.load('model/svmatn20_VII_morl_kfcvL'+str(i+1)+'_'+str(j)+'.joblib')
        #clf = joblib.load('model/svmatn20_VII_morl_shspcvL'+str(i+1)+'_'+str(j)+'.joblib')
        
        tepred = clf.predict(xdata[cvfolds[j]])
        
        print('%s\n' %(j+1),confusion_matrix(ydata[cvfolds[j]], tepred))
        tescore = accuracy_score(ydata[cvfolds[j]], tepred)
        sad = set(ydata[cvfolds[j]])-set(tepred)
        sad = list(sad)
        
        print('test acc: %.2f%%, never predicted: %s'
              %(tescore*100, sad))
        
        scores.append(tescore*100)
        # input()

    print('avg acc: %.2f%%' %np.mean(scores))
'''
# SVM yang diuji dengan statistical features yang diekstrak melalui DWT
#for i in range(5):
for i in range(1):
    cvfolds = np.load('cvfolds/kfcvU'+str(i+1)+'.npy')
    #cvfolds = np.load('cvfolds/shspcvU'+str(i+1)+'.npy')
    print('cvfolds/cvfoldsU'+str(i+1)+'.npy')
    scores = []
    for j in range(len(cvfolds)):
        clf = joblib.load('model/svmdwt_db2_kfcvL'+str(i+1)+'_'+str(j)+'.joblib')
        #clf = joblib.load('model/svmdwt_db2_shspcvL'+str(i+1)+'_'+str(j)+'.joblib')
        tepred = clf.predict(xdata[cvfolds[j]])

        print('%s\n' %(j+1),confusion_matrix(ydata[cvfolds[j]], tepred))
        tescore = accuracy_score(ydata[cvfolds[j]], tepred)
        sad = set(ydata[cvfolds[j]])-set(tepred)
        sad = list(sad)
    
        print('test acc: %.2f%%, never predicted: %s'
              %(tescore*100, sad))
        
        scores.append(tescore*100)
        # input()

    print('avg acc: %.2f%%' %np.mean(scores))
