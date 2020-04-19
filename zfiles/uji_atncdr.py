# -*- coding: utf-8 -*-

import h5py as h5
import numpy as np
from keras.models import Model
from keras import backend as bcknd
from keras.models import load_model

# %% Baca data

#f = h5.File('cwt181morl_fea.mat','r')
f = h5.File('cwt181morlunpre_fea.mat','r')
data = f.get('data_energy')
xdata = np.array(data)
xdata = np.transpose(data)

# %% Mulai uji model autoencoder

# Untuk data training
#for i in range(5):
for i in range(1):    
    for j in range(3):
        #ae = load_model('model/atncdr_aVII5_morl_kfcvL'+str(i+1)+'_'+str(j)+'.h5')
        #ae = load_model('model/atncdr_bVII10_morl_kfcvL'+str(i+1)+'_'+str(j)+'.h5')
        #ae = load_model('model/atncdr_cVII15_morl_kfcvL'+str(i+1)+'_'+str(j)+'.h5')
        ae = load_model('model/atncdr_dVII20_morl_kfcvL'+str(i+1)+'_'+str(j)+'.h5')
        
        #ae = load_model('model/atncdr_aVII5_morl_shspcvL'+str(i+1)+'_'+str(j)+'.h5')
        #ae = load_model('model/atncdr_bVII10_morl_shspcvL'+str(i+1)+'_'+str(j)+'.h5')
        #ae = load_model('model/atncdr_cVII15_morl_shspcvL'+str(i+1)+'_'+str(j)+'.h5')
        #ae = load_model('model/atncdr_dVII20_morl_shspcvL'+str(i+1)+'_'+str(j)+'.h5')
        
        enc = Model(ae.layers[0].input, ae.layers[4].output)
        edata = enc.predict(xdata)
        
        #np.save('encoded/atncdr_aVII5_morl_kfcv'+str(i+1)+'_'+str(j)+'.npy',edata)
        #np.save('encoded/atncdr_aVII5_morl_shspcv'+str(i+1)+'_'+str(j)+'.npy',edata)
        #print('encoded/atncdr_aVII5_morl_cvfolds'+str(i+1)+'_'+str(j)+'.npy has been saved')
        
        #np.save('encoded/atncdr_bVII10_morl_kfcv'+str(i+1)+'_'+str(j)+'.npy',edata)
        #np.save('encoded/atncdr_bVII10_morl_shspcv'+str(i+1)+'_'+str(j)+'.npy',edata)
        #print('encoded/atncdr_bVII10_morl_cvfolds'+str(i+1)+'_'+str(j)+'.npy has been saved')
        
        #np.save('encoded/atncdr_cVII15_morl_kfcv'+str(i+1)+'_'+str(j)+'.npy',edata)
        #np.save('encoded/atncdr_cVII15_morl_shspcv'+str(i+1)+'_'+str(j)+'.npy',edata)
        #print('encoded/atncdr_cVII15_morl_cvfolds'+str(i+1)+'_'+str(j)+'.npy has been saved')
        
        np.save('encoded/atncdr_dVII20_morl_kfcv'+str(i+1)+'_'+str(j)+'.npy',edata)
        #np.save('encoded/atncdr_dVII20_morl_shspcv'+str(i+1)+'_'+str(j)+'.npy',edata)
        #print('encoded/atncdr_dVII20_morl_cvfolds'+str(i+1)+'_'+str(j)+'.npy has been saved')
        
        bcknd.clear_session()
