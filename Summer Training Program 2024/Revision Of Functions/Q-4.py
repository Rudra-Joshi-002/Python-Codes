"""

Question-4: Write a function that is given a 9 x 9 potentially solved Sudoku and returns True if it is
solved correctly and False if there is a mistake. The Sudoku is correctly solved if there are
no repeated numbers in any row or any column or in any of the nine "blocks"

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
    
A=np.zeros((9,9))

num=0

print("Enter The Elements of 9x9 Sudoku: ")

for i in range(9):
    
    for j in range(9):
        
        num=int(input("Enter Here: "))
        
        A[i][j]=num
        
print("The Entered Sudoku Is: ")

print(A)

val=is_valid(A)

if val:
    
    print("Entered Suduko Is Correctly Solved.")
    
else:
    
    print("Entered Suduko Is not Correctly Solved.")
    

