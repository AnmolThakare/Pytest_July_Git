class Test_Credence:

    def test_mul_006(self):
        a = 3
        b = 4
        mul = a * b
        print("Mul of a & b is:" + str(mul))
        if mul == 12:
            assert True
        else:
            assert False


    def test_sub_007(self):
        a = 9
        b = 5
        sub = a - b
        print("Subtraction of a from b is:" +str(sub))
        if sub == a - b:
            assert True
        else:
            assert False
