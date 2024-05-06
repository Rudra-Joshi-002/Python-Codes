"""
Question-5: An integer is called squarefree if it is not divisible by any perfect squares other than 1.For
instance, 42 is squarefree because its divisors are 1, 2, 3, 6, 7, 21, and 42, and none of those
numbers (except 1) is a perfect square. On the other hand, 45 is not squarefree because it is
divisible by 9, which is a perfect square. Write a program that asks the user for an integer and
tells them if it is squarefree or not.

"""

import numpy as np

num=int(input("Enter any Integer: "))

boolean=0

for i in range(3,num):
    
    if num%i==0:
        
        sq=np.sqrt(i)
        
        isq=int(sq)
        
        if sq==isq:
            
            boolean=1
            
            break
if boolean:
    
    print("Entered Number: ",num," Is not a square free number")
    
else:
    
    print("Entered Number: ",num," Is a square free number")


