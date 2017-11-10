import unittest
from RecursiveMacroEconomics.ARModel import  ARModel
import numpy as np




class ARModelTest(unittest.TestCase):
    def test_illegal_input(self):
        #ar=ARModel(-1,12,12)
        self.assertRaises(Exception, lambda:ARModel(-3,np.array([1,2,3]),np.array([2,3])))
        #invalid length of param and inital value
        self.assertRaises(Exception, lambda:ARModel(2,np.array([1,2,4,3]),np.array([2,3])))
        #illegal order
        self.assertRaises(Exception,lambda:ARModel(1000,np.array([1,2,3]),np.array([2,3])))


        #self.assertRaises(Exception,lambda:ARModel(2,np.array([1,2,3]),np.array([1,3])))