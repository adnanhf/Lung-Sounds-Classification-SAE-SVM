# -*- coding: utf-8 -*-

import os
import scipy as sp
from sklearn.preprocessing import MaxAbsScaler

path = 'audiomat/'
filenames = os.listdir(path)
newsig = {}
for i in range(len(filenames)):
    sig = sp.io.loadmat(path+filenames[i],appendmat = False)
    au = sig['newau']
    newsig['newau'] = MaxAbsScaler().fit_transform(au)
    newsig['fs'] = sig['fs']
    sp.io.savemat('audionorm/'+filenames[i],mdict=newsig, appendmat = False)
