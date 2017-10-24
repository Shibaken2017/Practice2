import numpy as np
import matplotlib.pyplot as plt
from quantecon import LinearStateSpace
from scipy.stats import norm
import random


I=20
T=50


class Ensemble_plot:
    def __init__(self):
        print("nyan")



    def load_matrices(self,A,C,G):
        self.A=A
        self.C=C
        self.G=G

        self.ar=LinearStateSpace(A,C,G,mu_0=np.ones(4))
        x,y=self.ar.simulate(ts_length=2000)

        y=y.flatten()
        self.__y_max=1.3*np.max(y)
        self.__y_min=1.3*np.min(y)

    def set_plot(self):
        self.fig,self.ax=plt.subplots(figsize=(8,5))

        self.ax.set_ylim(self.__y_min,self.__y_max)
        self.ax.set_xlabel("time",fontsize=16)
        self.ax.set_ylabel("y_t",fontsize=16)

    def calc_ensemble_mean(self):

        self.ensemble_mean=np.zeros(T)
        for i in range(I):
            x,y=self.ar.simulate(ts_length=T)
            y=y.flatten()

            self.ax.plot(y,"c~",lw=0.8,alpha=0.5)
            self.ensemble_mean=self.ensemble_mean +  y

        self.ensemble_mean=self.ensemble_mean/I
        self.ax.plot(self.ensemble_mean,color="b",lw=2,alpha=0.8,label=r'$\bar y_t$')


    def calc_moment(self):
        print()
