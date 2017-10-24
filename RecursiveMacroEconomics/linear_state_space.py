import numpy as np
import matplotlib.pyplot as plt
from quantecon import LinearStateSpace
from scipy.stats import norm
import random

phi_0,phi_1,phi_2=1.1,0.8,-0.8

A=[[1,0,0],[phi_0,phi_1,phi_2],[0,1,0]]

C=np.ones((3,1))
G=[0,1,0]

ar=LinearStateSpace(A,C,G,mu_0=np.ones(3))
x,y=ar.simulate(ts_length=50)

fig,ax=plt.subplots(figsize=(8,4.6))




y=y.flatten()
print(y)
ax.plot(y,"-b",lw=2,alpha=0.7)
ax.grid()

ax.set_xlabel("time")
ax.set_ylabel("y")
plt.show()

##calc esemble_mean

esemble_mean=np.zeros(T)
I=20
T=50
for i in range(I):
    x,y=ar.simulate(ts_length=T)
    y=y.flatten()
    ax.plot(y,"-c",lw=0.8,alpha=0.5)
    ensemble_mean=ensemble_mean+y

ensemble_mean=ensemble_mean/I
ax.plot(ensemble_mean,color="b",lw=2,alpha=0.8,label="y_t")

    