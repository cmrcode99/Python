# Python Program to Find the Largest Among Three Numbers
a=float(input("Give a number"))
b=float(input("Give a number"))
c=float(input("Give a number"))
if b>c or c>b and (a>b or a>c):
    print("{} is the greatest number".format(a))
elif  b>a or a>b and (c>b or c>a):
    print("{} is the greatest number".format(c))
elif c>a or a>c and (b>c or b>a):
    print("{} is the greatest number".format(b))
    

