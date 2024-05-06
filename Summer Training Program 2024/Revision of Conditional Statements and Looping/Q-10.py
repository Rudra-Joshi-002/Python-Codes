"""
Question-10: Write a a program that finds all integer solutions to Pell's equation 
(x^2)-2(y^2)-1, where x and
y are between 1 and 100

"""

import numpy as np

x=np.arange(1,101)

y=np.arange(1,101)

print("The Solutions of equation (x^2)-2(y^2)-1 in integer range varying from 1 to 100 are: ")

for i in range(100):
    
    ans=((x[i])**2)-2*((y[i])**2)-1
    
    if ans==0:
        
        print("x= ",x[i]," y= ",y[i])

            