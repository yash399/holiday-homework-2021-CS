#a program to calculate in how many days a work will be completed by three persons A,B and C togther. take x days,ydays,zdays respectfully to do the job alone.
x = int(input("days taken by A"))
y = int(input("days taken by B"))
z = int(input("days taken by C"))
totalduration = x*y*z/(x*y+y*z+z*x)
print("total time taken by A,B,C togther is",round(totalduration,3))

