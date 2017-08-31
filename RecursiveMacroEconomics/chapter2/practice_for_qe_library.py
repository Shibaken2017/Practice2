import quantecon as qe
import numpy as np



def mc_sample_path(P,init=0,sample_size=1000):
    P=np.asarray(P)
    X=np.empty(sample_size,dtype=int)
    X[0]=init
    n=len(P)
    P_dist=[qe.DiscreteRV(P[i,:])for i in range(n)]
    for t in range(sample_size-1):
        X[t+1]=P_dist[X[t]].draw()

    return X


if __name__=="__main__":
    P=[[0.4,0.6],[0.2,0.8]]
    #X=mc_sample_path(P,sample_size=1000)

    mc=qe.MarkovChain(P,state_values=("employed","unemployed"))
    print(mc.simulate(ts_length=4,init="unemployed"))

