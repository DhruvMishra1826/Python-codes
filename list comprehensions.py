list=[3,5,2,55,6,33,11,56,33,55,44,243,545,32]
b=[i for i in list if i%2==1]
b.sort()
print(b)


def square(num):
    return num*num

l1=[1,2,3,4,5]
l2=[]
for i in l1:
    l2.append(i*i*i)

print(l2)


list1=[1,2,3,4,5,6,7,8,89,98]
list1=[i for i in list1 if i>10]
print(list1)

def mul(num):
    for i in range(1,11):
        print(f"{num}x{i}={num*i}\n")

mul(7)

l3=[str(i*7) for i in range(1,11)]
print(l3)
sentence="\n".join(l3)
print(sentence)

print("\n")

from functools import reduce
l4=[8, 94, 5, 10, 33, 4, 1 , 4]

def maximum(a,b):
    if (b>a):
        return b
    else:
        return a


var=reduce(maximum,l4)
print(var)