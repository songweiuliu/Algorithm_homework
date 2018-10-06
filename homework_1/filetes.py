# coding: utf-8
# liusongwei 21831068


#homework

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal


#Filtering processing
def fileter(path_):
    #read
    data=pd.read_csv(path_,header = None)
    data=data.iloc[1:,3]
    print(data,type(data))
    data.to_csv(r'.\data.csv',header=0,index=0)
    data_=np.array([float(i) for i in data.values])
    #filtering
    data_1=signal.medfilt(data_,101)
    return data_,data_1


# Visual waveform
def show(data_,data_1,start_):
    t=[x for x in range(len(data_[start_:]))]
    min=np.min(data_)
    max=np.max(data_)
    plt.plot(t,data_[start_:],'r--',t,data_1[start_:],'b-')
    plt.xlim(start_,len(t)-1)
    plt.ylim(min,max)
    plt.title("Plus_noise/filtered", fontsize=24)
    plt.xlabel("tims", fontsize=14)
    plt.ylabel("the Value ", fontsize=14)
    plt.legend(['origin_signal', 'filtered_signal'], loc='upper right')
    plt.tick_params(axis='both', which='major', labelsize=14)
    plt.show()



if __name__=='__main__':


    path=r'.\incX_1.csv'
    dat,dat1=fileter(path)
    show(dat,dat1,400)

