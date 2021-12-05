from os import add_dll_directory


class calculator:

    def __init__(self,a):
        self.a=a

    def square(self):
        print(f"square of {self.a} is {self.a**2}")

    def squareroot(self):
        print(f"square root of {self.a} is {self.a**0.5}")

    
    def cube(self):
        print(f"cube of {self.a} is {self.a**3}")
       
    
solve= calculator(16)
solve.square()
solve.squareroot()
solve.cube()

