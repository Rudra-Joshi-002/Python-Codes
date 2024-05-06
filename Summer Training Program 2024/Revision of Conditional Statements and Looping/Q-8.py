"""
Question-8: Write a program that starts with an 5 x 5 list of zeroes and randomly changes exactly ten of
those zeroes to ones.

"""

import numpy as np

var=np.zeros((5,5))

print("Value of var before randomly changing values: ")

print(var)

count=0

num=0

for i in range(5):
    
    for j in range(5):
        
        num=np.random.randint(0,2)
        
        if num==1 and count<10:
            
            var[i][j]=num
            
            num=0
            
            count+=1
            
            if count==10:
                
                break

        
print("Value of var after randomly changing values: ")

print(var)      