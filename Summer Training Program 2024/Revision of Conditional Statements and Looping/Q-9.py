"""
Question-9: Randomly generate a 9 x 9 list where the entries are integers between 1 and 9 with no repeat
entries in any row or in any column.

"""

import numpy as np

def is_valid(A):
    
    counterr=np.zeros(9)

    counterc=np.zeros(9)


    for i in range(9):
        
        for j in range(9):
            
            if A[i][j]==1:
                
                counterr[0]+=1
                
            elif A[i][j]==2:
                
                counterr[1]+=1
                
            elif A[i][j]==3:
                
                counterr[2]+=1
                
            elif A[i][j]==4:
                
                counterr[3]+=1
                
            elif A[i][j]==5:
                
                counterr[4]+=1
                
            elif A[i][j]==6:
                
                counterr[5]+=1
                
            elif A[i][j]==7:
                
                counterr[6]+=1
                
            elif A[i][j]==8:
                
                counterr[7]+=1
                
            elif A[i][j]==9:
                
                counterr[8]+=1
                
            #now column will be checked
            
            if A[j][i]==1:
                
                counterc[0]+=1
                
            elif A[j][i]==2:
                
                counterc[1]+=1
                
            elif A[j][i]==3:
                
                counterc[2]+=1
                
            elif A[j][i]==4:
                
                counterc[3]+=1
                
            elif A[j][i]==5:
                
                counterc[4]+=1
                
            elif A[j][i]==6:
                
                counterc[5]+=1
                
            elif A[j][i]==7:
                
                counterc[6]+=1
                
            elif A[j][i]==8:
                
                counterc[7]+=1
                
            elif A[j][i]==9:
                
                counterc[8]+=1
            
    coun9=0          
            
    for i in range(9):
        
        if counterr[i]==9 and counterc[i]==9:
            
            coun9+=1
            
    if coun9==9:
        
        return True

    else:
        
        return False
    
def generate_random(A):
    
    num=0
    
    for i in range(9):
        
        for j in range(9):
            
            num=np.random.randint(0,10)
            
            A[i][j]=num
            
            
    
    return A

A=np.zeros((9,9))

while(1):
    
    A=generate_random(A)
    
    print(A)
    
    val=is_valid(A)
    
    if val:
        
        break
    
print("The Required Matrix Is: ")

print(A)
            