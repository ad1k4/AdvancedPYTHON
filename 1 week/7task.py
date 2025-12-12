a=int(input("First number: "))
b=input("Operations: ")
c=int(input("Second numer: "))
if (b=='+'):
    print(a+c)
elif (b=='-'):
    print(a-c)
elif (b=='*'):
    print(a*c)
elif (b=='/'):
    if c==0:
        print("Not division to 0")
    else:
        print(a/c)
else:
    print("Invalid operations")