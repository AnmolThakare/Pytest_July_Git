class Test_Credence:

    def test_mul_004(self):
        a = 3
        b = 7
        mul = a * b
        print("Mul of a & b is:" +str(mul))
        if mul == 21:
            assert True
        else:
            assert False

    def test_sub_005(self):
        a = 12
        b = 7
        sub = a - b
        print("Subtraction of a from b:" +str(sub))
        if sub == 5:
            assert True
        else:
            assert False
