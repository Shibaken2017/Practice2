import numpy as np


class MarkovChain:
    def __init__(self):
        print("nyan")

    def calc(self,transition_mat):
        '''

        :param transition_mat:
        :return:
        '''
        print(transition_mat)
        self.__transion_mat=transition_mat

        self.check_input()
        la, v = np.linalg.eig(self.__transion_mat)
        print(la)
        print(v)


    def check_input(self):
        '''
        chcech wheher input matrix is a transition matrix and if not raise exception
        :return:
        '''
        self.__check_types()
        self.__check_matrix_size()
        self.__check_non_negative()
        self.__check_probability()


    def __check_types(self):
        if not type(self.__transion_mat) ==np.ndarray:
            raise Exception("input must be nparray")
        if not (self.__transion_mat.dtype!="float64"):
            raise Exception("input must be float 64 or int64 ")




    def __check_non_negative(self):
        '''

        :return:
        '''
        for row  in self.__transion_mat:
            for ele in row:
                if ele<0.0:
                    raise Exception("transition matri must not have any  nevative elements")


    def __check_probability(self):
        '''
        sum of each row mustbe 1
        :return:
        '''
        for i in range(self.__size[0]):
            rowsum=sum(self.__transion_mat[0])
            if not(rowsum==1.0 or rowsum==1):
                raise Exception("sum of each row must be 1")


    def __check_matrix_size(self,transition_matrix):
        self.__size=transition_matrix.shape
        if len(self.__size)!=2:
            raise Exception("size must be 2")
        if self.__size[0]!=self.__size[1]:
            raise Exception("transition  matrix musst  be square")




if __name__=="__main__":
    mat = np.array([[0.8, 0.2, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],dtype=float)
    print(type(mat))
    #test=MarkovChain()

    #test.calc(mat)


