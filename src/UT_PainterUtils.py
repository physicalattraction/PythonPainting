'''
Created on Jul 18, 2015

@author: Erwin Rossen
'''
import unittest
import PainterUtils

class Test(unittest.TestCase):

    def testRel2Abs_01(self):
        a = (0.5, 0.75)
        s = (1000, 2000)
        r = PainterUtils.rel2abs(rel_coordinate=a, size=s)
        e = (500, 1500)
        self.assertEqual(e, r)
    
    def testRel2Abs_02(self):
        a = (1 / 3, 2 / 3)
        s = (1000, 1000)
        r = PainterUtils.rel2abs(rel_coordinate=a, size=s)
        e = (333, 667)
        self.assertEqual(e, r)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
