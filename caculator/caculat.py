
class cacu:

    def myadd(a,b):
        """
        加法
        :return:
        """
        try:
            result = a+b
            return result
        except Exception as e:
            return e.args[0]

    def dividemethod(c,d):
        """
        除法
        :param c:
        :param d:
        :return:
        """
        if d == 0:
            print("分母不能为0")
        else:
            result1 = c/d
            return result1
