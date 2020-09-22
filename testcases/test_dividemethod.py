import unittest
from caculator import caculat

class testdivideclass(unittest.TestCase):
    def setUp(self):
        print("========开始=========")


    def test_divide1(self):
        ca = caculat.cacu
        self.assertEqual(ca.dividemethod(4,2),2)

    @unittest.expectedFailure
    def test_divide2(self):
        ca = caculat.cacu
        self.assertEqual(ca.dividemethod(6,0),0)

    @unittest.skip
    def test_divide3(self):
        pass

    def tearDown(self):
        print("==========结束==========")

if "__name__" == "__main__":
    unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(testdivideclass.test_divide1())
    runner = unittest.TextTestRunner(verbosity=0)
    runner.run(suite)