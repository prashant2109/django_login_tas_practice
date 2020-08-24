class A:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return self.a + other.b

    def __mul__(self, other):
        return self.a * other.b

    def __gt__(self, other):
        return self.a > other.b

class B:
    def __init__(self, b):
        self.b = b
    
if __name__ == '__main__':
    a_Obj = A(50)
    b_Obj = B(1)
    print(a_Obj+b_Obj)