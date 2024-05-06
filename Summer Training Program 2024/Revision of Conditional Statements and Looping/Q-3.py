"""

Question-3: Write a multiplication game program for kids. The program should give the player ten
randomly generated multiplication questions to do. After each, the program should tell them
whether they got it right or wrong and what the correct answer is.

"""

import numpy as np

op1=np.zeros(10)

op2=np.zeros(10)

for i in range(10):
    
    op1[i]=np.random.randint(1,100)
    
    op2[i]=np.random.randint(1,100)
    
result=op1*op2

for i in range(10):
    
    print("Enter the answer of ",op1[i],"x",op2[i]," : ")
    
    ans=int(input())
    
    if ans==result[i]:
        
        print("Entered Answer ",ans," is Correct Answer")
        
    else:
        
        print("Entered Answer is Incorrect.")
        
        print("Correct Answer is: ",result[i])
        
        
