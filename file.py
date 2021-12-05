f= open('sample.txt', 'r')
data=f.read()
print(data)
f.close()

f=open('another_file.txt', 'w')
text=f.write("I am 1826")
print(text)
f.close()

f=open('another_file.txt', 'a')
text=f.write(" I am appending")
print(text)
f.close()

with open('twinkle.txt', 'r') as f:
    t=f.read()
    if 'twinkle' in t:
        print("word is present")
    else:
        print("absent")

    if 'u' in t:
        print("word is present")
    else:
        print("absent")


with open('highscore_game checker.txt') as f:
    x=int(f.read())
    urscore=6889

if (urscore>x):
        with open('highscore_game checker.txt', 'a') as f:
            f.write(str(urscore))


with open('donkey.txt','r') as f:
   str= f.read()

str= str.replace("donkey","######")
with open('donkey.txt','w') as f:
    str=f.write(str)