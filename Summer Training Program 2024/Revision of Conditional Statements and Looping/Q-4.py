"""

Question-4: Write a program that lets the user play Rock-Paper-Scissors against the computer. There
should be five rounds, and after those five rounds, your program should print out who won
and lost or that there is a tie

"""

import numpy as np

comp=["r","p","s"]


comcount=0

ucount=0

print("For the given game Enter your response in small characters: s-> scissor, r-> rock, p-> paper")

for i in range(5):
    
    num=np.random.randint(0,3)
    
    print(comp[num])
    
    uresponse=input("Enter Your Response: ")
    
    if comp[num]=='r' and uresponse=='p':
        
        ucount+=1
        
    elif comp[num]=='r' and uresponse=='s':
        
        comcount+=1
        
    elif comp[num]=='p' and uresponse=='s':
        
        ucount+=1
        
    elif comp[num]=='p' and uresponse=='r':
        
        comcount+=1
        
    elif comp[num]=='s' and uresponse=='p':
        
        comcount+=1
        
    elif comp[num]=='s' and uresponse=='r':
        
        ucount+=1

if comcount<ucount:
    
    print("Scores Are User: ",ucount," Computer: ",comcount)
    
    print("Congratulations You Won...!!!")

elif comcount>ucount:
    
    print("Scores Are User: ",ucount," Computer: ",comcount)
    
    print("You Loose...Better Luck Next Time...")

else:
    
    print("Scores Are User: ",ucount," Computer: ",comcount)
    
    print("Its A Tie...")    