#solve ricatti equation by iterating algorthm

#R:n*n,Q:k*k,H:k*n,
# A*n*n,B:n*k,P:n*n
import numpy as np



class RicattiEquation:
    def __init__(self,beta,A,B,R,Q,H):
        print("")
        self.beta=beta
        self.A=A
        self.B=B
        self.Q=Q
        self.P=0
        self.H=H

    def check_input(self):
        self.check_beta()
        self.check_matrix_type_shape(self.A)
        self.check_matrix_type_shape(self.B)
        self.check_matrix_type_shape(self.Q)
        self.check_matrix_type_shape(self.H)




    def check_beta(self):
        if not(type(self.beta)==int or type(self.beta)==float):
            raise Exception("beta must be int or float")

    def check_square_matrix(self,input_matrix):
        if not input_matrix.shape[0]==input_matrix.shape[1]:
            raise Exception("matrix must be square")


    def check_matrix_size(self):
        self.n=self.A.shape[0]
        self.k=self.B.shape[1]

        #A:n*n
        self.check_square_matrix(self.A)
        self.check_square_matrix(self.Q)
        self.check_sqruaare_matrix(sefl.P)





    def check_matrix_type_shape(self,input_matrix):
        '''

        :param input_matrix:
        :return:
        '''
        if not type(input_matrix)==np.ndarray:
            raise Exception("must be np.ndarray")
        if not len(input_matrix.shape)==2:
            raise Exception("len must be 2")


