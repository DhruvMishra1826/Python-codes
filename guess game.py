import random


count=0
a=0
randno=1
g=1
while g==1:
    while (randno>a):
        randno= random.randint(1,100)
        a=int(input("Enter any number from 1 to 100 : "))
        if (randno>a):
            print(f"its lower as computer choosen {randno}\n")
            count=count+1 

    if (randno<a):
        print(f"its higher  as computer choosen {randno} and u got this after {count+1} chances\n Thank you for playing")


    if (count+1==1):
        print("you are super hero")
    elif (count+1>1 and count+1<=5):
        print("6th sense is average")
    else:
        print("weak 6th sense : )")

    b=input("Do u want to play again write yes or no: ")
    if b=='yes':
        g=1
        a=0
        randno=1
        count=0
    else:
        g=0
        
