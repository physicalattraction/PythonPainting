'''
Created on May 31, 2015

@author: Erwin Rossen
'''
import unittest
from SpiralPainter import SpiralPainter


class Test_denormalize_W(unittest.TestCase):
    
    def setUp(self):
        self.sut = SpiralPainter()
        self.sut.W = 600
        self.sut.H = 800
    
    def test_normal_behavior(self):
        test_values = {0:300, -1:0, 1:600}
        for (a, e) in test_values.items():
            r = self.sut._denormalize_W(a)
            msg = "Input: {}. Received value: {}. Expected value: {}".format(a, r, e)
            self.assertEqual(r, e, msg)
            
class Test_denormalize_H(unittest.TestCase):
    
    def setUp(self):
        self.sut = SpiralPainter()
        self.sut.W = 600
        self.sut.H = 800
    
    def test_normal_behavior(self):
        test_values = {0:400, -1:0, 1:800}
        for (a, e) in test_values.items():
            r = self.sut._denormalize_H(a)
            msg = "Input: {}. Received value: {}. Expected value: {}".format(a, r, e)
            self.assertEqual(r, e, msg)

class Test_normalize_W(unittest.TestCase):
    
    def setUp(self):
        self.sut = SpiralPainter()
        self.sut.W = 600
        self.sut.H = 800
    
    def test_normal_behavior(self):
        test_values = {300:0, 0:-1, 600:1}
        for (a, e) in test_values.items():
            r = self.sut._normalize_W(a)
            msg = "Input: {}. Received value: {}. Expected value: {}".format(a, r, e)
            self.assertEqual(r, e, msg)
                
class Test_normalize_H(unittest.TestCase):
    
    def setUp(self):
        self.sut = SpiralPainter()
        self.sut.W = 600
        self.sut.H = 800
    
    def test_normal_behavior(self):
        test_values = {400:0, 0:-1, 800:1}
        for (a, e) in test_values.items():
            r = self.sut._normalize_H(a)
            msg = "Input: {}. Received value: {}. Expected value: {}".format(a, r, e)
            self.assertEqual(r, e, msg)

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
