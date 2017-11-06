import numpy as np



'''
predict future values from current and past y's value

'''


class ARModel:
    def __init__(self,order,param,initial):
        '''

        :param order:order of ar model
        :param param: param of ar
        :param initial: initial value of ar
        '''
        self.order=order

        self.param=param
        self.initial=initial

        self.order_check()

        self.pred=self.initial

    def predict(self):
        st=0
        ed=self.order


        for i in range(100):
            print(self.param[1:])
            print(self.pred[0:])
            #np.dot(self.param[1:],self.predict[0:2])
            predict=self.param[0]+np.dot(self.param[1:],self.pred[st:ed])
            self.pred=np.append(self.pred,predict)
            st+=1
            ed+=1

        print(self.pred)





    def param_initial_check(self):
        if not (len(self.initial)==self.order and type(self.initial)==np.ndarray):
            raise Exception("(1)len of initial and order must be the same(2)initial must be ndarray")

        if not (len(self.param)==(self.order+1)and type(self.param)==np.ndarray):
            raise  Exception("(1)len of pram must be the same as order+1(2)param must be ndarray")















    def order_check(self):
        if type(self.order) !=int:
            raise Exception("order must be integer")
        if not(0<self.order and self.order<21):
            raise Exception("order must be integer and 0< order<21")



if __name__=="__main__":
    test=ARModel(2,np.array([1,2,3]),np.array([1,1]))
    test.predict()