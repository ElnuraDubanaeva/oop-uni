import numpy as np
from random import randint

class Matrix :
    def __init__(self , hight , lenth):
        self.higth = hight
        self.lenth = lenth

    def numbers (self):
        matrix1 =[]
        for i in self.hight:
            matrix1.append(randint(1, 100))
        for i in self.lenth:
            matrix1.append(randint(10,50))
    def np (self):
        a = np.arange(matrix1).reshape(self.hight, self.lenth)
        return a


matrix1 = Matrix(3,4)
print (matrix1.np())

