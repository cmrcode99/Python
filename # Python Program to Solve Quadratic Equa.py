# Python Program to Solve Quadratic Equation
import math
a=float(input("Give me a "))
b=float(input("Give me b "))  
c=float(input("Give me c "))    

d=(-b-((b**2-4*a*c)**0.5))/2*a
e=(-b+((b**2-4*a*c)**0.5))/2*a
if(d==e):
    print(d)
elif(d!=e):
    print(d)
    print(e)


