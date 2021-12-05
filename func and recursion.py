

def sum(n):
    if (n<1):
        return n

    return n + sum(n-1)
    

n= int(input("Enter the number:"))
p= sum(n)
print(p)


for i in range(3):
    print("*"*(3-i), end="\n")


