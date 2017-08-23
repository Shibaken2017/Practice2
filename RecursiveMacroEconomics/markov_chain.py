import numpy as np

def calc(prob_matrix):
    '''
    calculate the stationary state from a markov transition matrix


    :param prob_matrix:
    :return:
    '''
    if not type(prob_matrix)=="numpy.ndarray":
        raise Exception("input must be nparray")


    la, v = np.linalg.eig(prob_matrix)
    print(la)
    print(v)


def check_matrix_size():


if __name__=="__main__":
    a = np.array([[0.8, 0.2, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])

    calc(a)

