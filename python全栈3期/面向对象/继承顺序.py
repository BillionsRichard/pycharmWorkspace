"""
广度优先: 新式类（Python3）                  F->D->B->E->C->A
深度优先： 经典类（python2，不继承自object类）F->D->B->A->E->C

 A
| \
B  C
|  \
D  E
\  /
 \/
 F

"""
from pprint import pprint as pp

class A:
    def test(self):
        print('A')

class B(A):
    def test(self):
        print('B')
    pass

class C(A):
    def test(self):
        print('C')

class D(B):
    pass
    # def test(self):
    #     print('D')

class E(C):
    def test(self):
        print('E')
    pass


class F(D, E):
    pass
    # def test(self):
    #     print('F')

f1 = F()
f1.test()

pp(F.__mro__)

