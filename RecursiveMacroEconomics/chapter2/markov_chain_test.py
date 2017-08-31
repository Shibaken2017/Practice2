import unittest

import numpy as np

from RecursiveMacroEconomics.chapter2.markov_chain import MarkovChain


class test_markov_chain(unittest.TestCase):

    def test_valid_input(self):
        markov = MarkovChain()
        #mat = np.array([[1.j, -1.j, 1.0], [0.2, 0.2, 0.6], [0.3, 0.3, 0.4]])



    


    def test_complex_matrix(self):
        markov=MarkovChain()
        mat= np.array([[1.j,-1.j,1.0],[0.2,0.2,0.6],[0.3,0.3,0.4]])
        self.assertRaises(Exception, lambda: markov.set_matrix(mat))


    def test_none_transition_matrix(self):
        markov=MarkovChain()
        mat=np.array([[1.1,1.2,1.3],[1.0,0.2,0.3],[1.0,0.0,0.0]])
        self.assertRaises(Exception, lambda: markov.set_matrix(mat))


    def test_none_squre_matrix(self):
        markov=MarkovChain()
        mat = np.array([[0.8, 0.2, 0.0], [0.0, 1.0, 0.0]],dtype=float)
        self.assertRaises(Exception, lambda: markov.set_matrix(mat))

    def test_negative_matrix(self):
        markov = MarkovChain()
        mat = np.array([[0.5, 0.2, 0.3], [1.0, -1.0, 1.0],[0.2,0.4,0.4]],dtype=float)
        self.assertRaises(Exception, lambda: markov.set_matrix(mat))

    def test_none_input(self):
        markov=MarkovChain()
        test=None
        print(markov)
        self.assertRaises(Exception, lambda: markov.set_matrix(test))



if __name__ == '__main__':
  unittest.main()