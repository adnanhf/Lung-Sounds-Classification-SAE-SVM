# -*- coding: utf-8 -*-

import h5py as h5
import numpy as np
from sklearn import svm
from sklearn.externals import joblib
# from sklearn.metrics import accuracy_score, confusion_matrix, f1_score

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

# %% Mulai latih SVM

'''
# SVM yang dilatih dengan features yang direduksi oleh autoencoder
#for i in range(5):
for i in range(1):    
    cvfolds = np.load('cvfolds/kfcvL'+str(i+1)+'.npy')
    #cvfolds = np.load('cvfolds/shspcvL'+str(i+1)+'.npy')
    print('cvfolds/cvfoldsL'+str(i+1)+'.npy')
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
        
        #clf = svm.SVC(C=1,gamma='scale')
        clf = svm.SVC(C=10000,gamma='scale')
        clf.fit(xdata[cvfolds[j]],ydata[cvfolds[j]])
        
        #joblib.dump(clf,'model/svmatn5_VII_morl_kfcvL'+str(i+1)+'_'+str(j)+'.joblib')
        #joblib.dump(clf,'model/svmatn5_VII_morl_shspcvL'+str(i+1)+'_'+str(j)+'.joblib')
        #print('model/svm5_VII_morl_cvfoldsL'+str(i+1)+'_'+str(j)+'.joblib has saved')
        
        #joblib.dump(clf,'model/svmatn10_VII_morl_kfcvL'+str(i+1)+'_'+str(j)+'.joblib')
        #joblib.dump(clf,'model/svmatn10_VII_morl_shspcvL'+str(i+1)+'_'+str(j)+'.joblib')
        #print('model/svm10_VII_morl_cvfoldsL'+str(i+1)+'_'+str(j)+'.joblib has saved')
        
        #joblib.dump(clf,'model/svmatn15_VII_morl_kfcvL'+str(i+1)+'_'+str(j)+'.joblib')
        #joblib.dump(clf,'model/svmatn15_VII_morl_shspcvL'+str(i+1)+'_'+str(j)+'.joblib')
        #print('model/svmatn15_VII_morl_cvfoldsL'+str(i+1)+'_'+str(j)+'.joblib has saved')
        
        joblib.dump(clf,'model/svmatn20_VII_morl_kfcvL'+str(i+1)+'_'+str(j)+'.joblib')
        #joblib.dump(clf,'model/svmatn20_VII_morl_shspcvL'+str(i+1)+'_'+str(j)+'.joblib')
        #print('model/svmatn20_VII_morl_cvfoldsL'+str(i+1)+'_'+str(j)+'.joblib has saved')
'''
# SVM yang dilatih dengan statistical features yang diekstrak melalui DWT
#for i in range(5):
for i in range(1):    
    cvfolds = np.load('cvfolds/kfcvL'+str(i+1)+'.npy')
    #cvfolds = np.load('cvfolds/shspcvL'+str(i+1)+'.npy')
    print('cvfolds/cvfoldsL'+str(i+1)+'.npy')
    for j in range(len(cvfolds)):
        #clf = svm.SVC(C=1,gamma='scale')
        clf = svm.SVC(C=10000,gamma='scale')
        clf.fit(xdata[cvfolds[j]],ydata[cvfolds[j]])
        
        joblib.dump(clf,'model/svmdwt_db2_kfcvL'+str(i+1)+'_'+str(j)+'.joblib')
        #joblib.dump(clf,'model/svmdwt_db2_shspcvL'+str(i+1)+'_'+str(j)+'.joblib')
        print('model/svmdwt_db2_cvfoldsL'+str(i+1)+'_'+str(j)+'.joblib has saved')
