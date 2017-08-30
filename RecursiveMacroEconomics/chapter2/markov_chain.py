import numpy as np


class MarkovChain:
    def __init__(self):
        print("nyan")



    def calc_n_step_ahead_distribution(self,transition_mat,initial_distribution,num_of_transition):
        '''

        :param transition_mat:
        :param initial_distribution:
        :param num_of_transition:
        :return:
        '''
        self.set_matrix(transition_mat)
        self.__initial_distribution=initial_distribution

        tmp_init=self.__initial_distribution
        tmp_output=None
        self.__transposed=np.transpose(self.__transion_mat)
        for i in range(num_of_transition):
            tmp_output=np.dot(self.__transposed,tmp_init)
            #print(tmp_output)
            tmp_init=tmp_output

        print(tmp_output)

        return tmp_output

    def set_initial_distribution(self,initial_distribution):
        self.__initial_distribution=initial_distribution
        self.check_initial_distribution()


    def check_initial_distribution(self):
        self.__check__types(self.__initial_distribution)



            #if type(self.__transion_mat) != np.ndarray:
            #    raise Exception("input must be nparray")
            #if (self.__transion_mat.dtype != "float64"):
             #   raise Exception("input must be float64 ")





    def set_matrix(self,transition_mat):
        self.__transion_mat=transition_mat
        self.check_input_matrix()




    def calc_statioanry_distribution(self,transition_mat):
        '''

        :param transition_mat:
        :return:
        '''
        self.set_matrix(transition_mat)
        self.__la, self.__vec = np.linalg.eig(np.transpose(self.__transion_mat))

        ##固有ベクトルに府の要素がある場合にはそれを除くように修正する必要がある
        self.__normalize_vector()
        print(self.__la)
        print(self.__vec)




    def __normalize_vector(self):

        for num in range(len(self.__vec)):
            self.__vec[num]=self.__vec[num]/np.sum(self.__vec[num])






    def check_input_matrix(self):
        '''
        chcech wheher input matrix is a transition matrix and if not raise exception
        :return:
        '''
        self.__check__types(self.__transion_mat)
        self.__check_matrix_size()
        self.__check_matrix_non_negative()
        self.__check_matrix_probability()


    def __check__types(self,input_mat):
        if  type(input_mat) !=np.ndarray:
            raise Exception("input must be nparray")
        if (input_mat.dtype!="float64"):
            raise Exception("input must be float64 ")




    def __check_matrix_non_negative(self):
        '''

        :return:
        '''
        for row  in self.__transion_mat:
            for ele in row:
                if ele<0.0:
                    raise Exception("transition matri must not have any  nevative elements")


    def __check_initial_distribution_size(self):
        self.__size = self.__initial_distribution.shape

        if len(self.__size) !=2 :
            raise Exception("initial_distribution's shape must be 2")
        if self.__size[1] != 1:
            raise Exception("initail_distribution must be n*1 matrix")






    def __check_matrix_probability(self):
        '''
        sum of each row mustbe 1
        :return:
        '''
        for i in range(self.__mat_size[0]):
            rowsum=sum(self.__transion_mat[0])
            if not(rowsum==1.0 or rowsum==1):
                raise Exception("sum of each row must be 1")


    def __check_matrix_size(self):
        self.__mat_size=self.__transion_mat.shape

        if len(self.__mat_size)!=2:
            raise Exception("size must be 2")
        if self.__mat_size[0]!=self.__mat_size[1]:
            raise Exception("transition  matrix musst  be square")




if __name__=="__main__":
    mat = np.array([[0.8, 0.2, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],dtype=float)
    #print(np.transpose(mat))

    markov=MarkovChain()
    #(markov.calc_statioanry_distribution(mat))

    markov.calc_n_step_ahead_distribution(mat,np.array([[0.4],[0.1],[0.5]],dtype=float),4000)


