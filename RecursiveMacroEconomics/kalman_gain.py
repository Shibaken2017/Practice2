import numpy as np
import  matplotlib.pyplot as plt
from quantecon import Kalman
from quantecon import LinearStateSpace
from scipy.stats import norm

theta=10
A,C,G,H=1,0,1,1
#mu_0は  x0 の初期分布の平均パラメータ
ss=LinearStateSpace(A,C,G,H,mu_0=theta)

x_hat_0,Sigma_0=8,1
kalman=Kalman(ss,x_hat_0,Sigma_0)



N=5
x,y=ss.simulate(N)
y=y.flatten()
print(y)


#
fig,ax=plt.subplots(figsize=(10,8))
xgrid=np.linspace(theta-5,theta+2,200)

for i in range(N):

    m,v=[float(z) for z in (kalman.x_hat,kalman.Sigma)]
    print(m)
    ax.plot(xgrid,norm.pdf(xgrid,loc=m,scale=np.sqrt(v)),label=r't={}'.format(i))
    kalman.update(y[i])


plt.show()