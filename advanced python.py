try:
    a=input("enter the number: ")
    a=int(a)
    print(a)
except Exception as e:
    print(f"your input resulted in an error : {e}")

print("Thank u")