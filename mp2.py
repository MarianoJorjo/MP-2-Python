import numpy as np
import math 
print("Input first points")
x1 = int(input())
y1 = int(input())
print("Input second points")
x2 = int(input())
y2 = int(input())
print("Input third points")
x3 = int(input())
y3 = int(input())
Z = np.array([(x1**2 + y1**2,x1,y1,1),(x2**2 + y2**2,x2,y2,1),(x3**2+y3**2,x3,y3,1)])
print("The matrix \n",Z) #the matrix

#the x center
m12 = Z[:,[0,2,3]]
d12 = np.linalg.det(m12)
m11 = Z[:,[1,2,3]]
d11 = np.linalg.det(m11)
x = 1/2 * (d12/d11)

xx = round(x)


#the y center
m13 = Z[:,[0,1,3]]
d13 = np.linalg.det(m13)
y = (-1/2) * (d13/d11)
yy = round(y)



m14 = Z[:,[0,1,2]]
d14 = np.linalg.det(m14)
print("the center is: (",xx,yy,")")
r2 = xx**2 + yy**2 + (d14/d11)
r = math.sqrt(r2)
print("Radius is: ",r)

D = 2*(-xx)
E = 2*(-yy) 
F = xx**2 + yy**2 - r**2

V = ([D,E,F])
print("The coefficients are", V)
