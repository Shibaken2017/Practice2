from RecursiveMacroEconomics.markov_chain import MarkovChain

import unittest
import numpy as np

class test_markov_chain(unittest.TestCase):
    def setUp(self):
        self.markov=MarkovChain()


    def test_none_squre_matrix(self):
        markov=MarkovChain()
        mat = np.array([[0.8, 0.2, 0.0], [0.0, 1.0, 0.0]],dtype=float)
        self.assertRaises(Exception, lambda: markov.calc(mat))



    def test_none_input(self):
        markov=MarkovChain()
        test=None
        print(markov)
        self.assertRaises(Exception, lambda: markov.calc(test))

        '''
  def test_exception(self):
    self.assertRaises(MyException, self.target.something())


'''

if __name__ == '__main__':
  unittest.main()