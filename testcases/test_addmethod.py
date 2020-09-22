import unittest
from parameterized import  parameterized,param
from caculator.caculat import cacu


class testAddclass(unittest.TestCase):
    def setUp(self):
        print("===========测试开始============")

    @parameterized.expand(
        [param(1,1,2),
         param(1.1,98.9,100)])
    def test_add(self,first,second,result):
        ca = cacu
        self.assertEqual(ca.myadd(first,second),result)


    def tearDown(self):
        print("===========测试结束============")

if "__name__" == "__main__":
    unittest.main()