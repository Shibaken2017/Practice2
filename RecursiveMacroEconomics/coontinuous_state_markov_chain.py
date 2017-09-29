import  numpy  as np
import matplotlib.pyplot as plt

from scipy.stats import norm,gaussian_kde
from quantecon import LAE

phi=norm()
n=500
theta=0.8

d=np.sqrt(1-theta**2)
delta=theta/d

def psi_star(y):
    return 2*norm.pdf(y)*norm.cdf(delta*y)

def p(x,y):
    return phi.pdf((y-theta*np.abs(x))/d)/d

#generate n random number from normal distribution
Z=phi.rvs(n)

X=np.empty(n)


for t in range(n-1):
    X[t+1]=theta*np.abs(X[t])+d*Z[t]

psi_est=LAE(p,X)
k_est=gaussian_kde(X)


fig,ax=plt.subplots(figsize=(10,7))
#generate 200 numbers from -3 to 3
ys=np.linspace(-3,3,200)

ax.plot(ys,psi_star(ys),"b-",lw=2,alpha=0.6,label="true")
ax.plot(ys,psi_est(ys),"g-",lw=2,alpha=0.6,label="look ahead estimate")
ax.plot(ys,k_est(ys),"k-",lw=2,alpha=0.6,label="kernel based estimate")
ax.legend(loc="upper left")
#.show()


