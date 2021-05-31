#write a python program to calculate the amount payable if monet has been lent on simple intrest.
p = float(input("enter principal amount"))
r = float(input("enter annual rate of interest"))
t = float(input("enter time in number of years"))
si = p*r*t/100
print("simple interest is",si)
