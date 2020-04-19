# -*- coding: utf-8 -*-

import h5py as h5
import numpy as np
from keras.models import Model
from keras import backend as bcknd
from keras.layers import Input, Dense

# %% Baca data dan cvfolds

#f = h5.File('cwt181morl_fea.mat','r')
f = h5.File('cwt181morlunpre_fea.mat','r')
data = f.get('data_energy')
xdata = np.array(data)
xdata = np.transpose(data)

# %% Mulai latih Autoencoder sebanyak N cvfolds

#for i in range(5):
for i in range(1):    
    # cvfolds
    cvfoldsL = np.load('cvfolds/kfcvL'+str(i+1)+'.npy')
    #cvfoldsL = np.load('cvfolds/shspcvL'+str(i+1)+'.npy')
    print('cvfolds/cvfoldsL'+str(i+1)+'.npy')
    for j in range(len(cvfoldsL)):
        x,y = np.shape(xdata[cvfoldsL[j]])
        del x
        
        inpts = Input(shape=(y,), name='input')
        encoded = Dense(100, activation='relu', name='encoder1')(inpts)
        encoded = Dense(50, activation='relu', name='encoder2')(encoded)
        encoded = Dense(25, activation='relu', name='encoder3')(encoded)
        #coded = Dense(5, activation='relu', name='code')(encoded)
        #coded = Dense(10, activation='relu', name='code')(encoded)
        #coded = Dense(15, activation='relu', name='code')(encoded)
        coded = Dense(20, activation='relu', name='code')(encoded)
        decoded = Dense(25, activation='relu', name='decoder1')(encoded)
        decoded = Dense(50, activation='relu', name='decoder2')(decoded)
        decoded = Dense(100, activation='relu', name='decoder3')(decoded)
        otpts = Dense(y, activation='sigmoid', name='output')(decoded)
        
        ae = Model(inpts, otpts)
        enc = Model(inpts,coded)
        ae.compile(optimizer='rmsprop',loss='binary_crossentropy')
        
        #report = ae.fit(xdata[cvfoldsL[j]],xdata[cvfoldsL[j]],epochs=50,batch_size=10,verbose=1)
        #report = ae.fit(xdata[cvfoldsL[j]],xdata[cvfoldsL[j]],epochs=100,batch_size=10,verbose=1)
        #report = ae.fit(xdata[cvfoldsL[j]],xdata[cvfoldsL[j]],epochs=300,batch_size=10,verbose=1)
        #report = ae.fit(xdata[cvfoldsL[j]],xdata[cvfoldsL[j]],epochs=500,batch_size=10,verbose=1)
        #report = ae.fit(xdata[cvfoldsL[j]],xdata[cvfoldsL[j]],epochs=1000,batch_size=10,verbose=1)
        #report = ae.fit(xdata[cvfoldsL[j]],xdata[cvfoldsL[j]],epochs=1300,batch_size=10,verbose=1)
        #report = ae.fit(xdata[cvfoldsL[j]],xdata[cvfoldsL[j]],epochs=1500,batch_size=10,verbose=1)
        report = ae.fit(xdata[cvfoldsL[j]],xdata[cvfoldsL[j]],epochs=2000,batch_size=10,verbose=1)
        
        #ae.save('model/atncdr_aVII5_morl_kfcvL'+str(i+1)+'_'+str(j)+'.h5')
        #ae.save('model/atncdr_aVII5_morl_shspcvL'+str(i+1)+'_'+str(j)+'.h5')
        #print('model/atncdr_aVII5_morl_cvfoldsL'+str(i+1)+'_'+str(j)+'.h5 has saved')
        
        #ae.save('model/atncdr_bVII10_morl_kfcvL'+str(i+1)+'_'+str(j)+'.h5')
        #ae.save('model/atncdr_bVII10_morl_shspcvL'+str(i+1)+'_'+str(j)+'.h5')
        #print('model/atncdr_bVII10_morl_cvfoldsL'+str(i+1)+'_'+str(j)+'.h5 has saved')
        
        #ae.save('model/atncdr_cVII15_morl_kfcvL'+str(i+1)+'_'+str(j)+'.h5')
        #ae.save('model/atncdr_cVII15_morl_shspcvL'+str(i+1)+'_'+str(j)+'.h5')
        #print('model/atncdr_cVII15_morl_cvfoldsL'+str(i+1)+'_'+str(j)+'.h5 has saved')
        
        ae.save('model/atncdr_dVII20_morl_kfcvL'+str(i+1)+'_'+str(j)+'.h5')
        #ae.save('model/atncdr_dVII20_morl_shspcvL'+str(i+1)+'_'+str(j)+'.h5')
        #print('model/atncdr_dVII20_morl_cvfoldsL'+str(i+1)+'_'+str(j)+'.h5 has saved')
        bcknd.clear_session()