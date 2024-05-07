"""

Question-2: Write a program that generates 100 integers randomly that are either 0 or 1. Then find the
longest run of zcros, the largest number of zeros 1n a row For instance, the longest run of
zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4

"""
import numpy as np

A=[]

for i in range(100):
    
    A.append(np.random.randint(0,2))
    
print("The Randomly Generated 100 integers that either 0 or 1 Are: ")

print(A)

Max=0

counter=0

for i in range(len(A)-1):
    
    if A[i]==0 and A[i+1]==0:
        
        counter+=1
        
        if counter>=Max:
            
            Max=counter
        
    else:
        
        counter=0

print("In the given generated integers the largest number of zeroes in Row are: ",Max+1)          
            
        
        