#name= input("enter ur name")
#print("good morning, " +name)

atapata= input("name\n")
date= input("date")

c= '''Good morning, <|name|> today is <|tithi|> '''
c= c.replace("<|name|>", atapata)
c= c.replace("<|tithi|>", date)

print(c)

friend=["ram", "shyam", "krishna", "balram", "narayan"]
print(friend[3])


