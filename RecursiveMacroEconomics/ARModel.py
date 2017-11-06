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


    def predict(self):

        







    def param_initial_check(self):
        if not (len(self.initial)==self.order and type(self.initial)==np.ndarray):
            raise Exception("(1)len of initial and order must be the same(2)initial must be ndarray")

        if not (len(self.param)==(self.order+1)and type(self.param)==np.ndarray):
            raise  Exception("(1)len of pram must be the same as order+1(2)param must be ndarray")















    def order_check(self):
        if type(self.order) !="int":
            raise Exception("order must be integer")
        if not(0<self.order and self.order<21):
            raise Exception("order must be integer and 0< order<21")



