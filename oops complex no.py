class complex:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def __add__(self,c):
        return complex(self.a +c.a , self.b+c.b)
    
    def __mul__(self,c):
        return complex(self.a*c.a - self.b*c.b , self.a*c.b + self.b*c.a)

    def __str__(self):
        return f"{self.a} + {self.b}i"



e=complex(2,3)
f=complex(2,-3)
print(e)
print(f)
print(f+e)
print(f * e)

