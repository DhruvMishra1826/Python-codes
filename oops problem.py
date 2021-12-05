class vec1:
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"

class vec2(vec1):
    def __init__(self,i,j,k):
        self.icap=i
        self.jcap=j
        self.kcap=k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"


v1= vec1(1,2)
v2= vec2(5,8,6)
print(v1)
print(v2)
    