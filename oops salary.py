class employee:
    
        base=50000
        increament=1.5
        @property
        def salary(self):
            return self.base*self.increament

        @salary.setter
        def salary(self, sai):
            self.increament=sai/self.base

a= employee()
print(f"salary after increament={a.salary}\n")
a.salary=int(input(f"the new salary: "))

print(f"increament is of : {a.increament}")