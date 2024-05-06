"""

Question-7 Write a program that asks the user to enter a password. If the user enters the right password,
the program should tell them they are logged in to the system. Otherwise, the program should ask
them to reenter the password. The user should only get five tries to enter the password, after
which point the program should tell them that they are kicked off of the system. (Use While
loop)

"""

PASSW="123456"

n=0

while n<5:
    
    upass=input("Enter Password: ")
    
    if upass==PASSW:
        
        print("Correct Password You Are Logged into the System")
        
        break
    
    else:
        
        n+=1
        
        print("Password Incorrect Enter Again")
        
        print("Availabe Number of Trials: ",5-n)
        
        if n==5:
            
            print("Too Many Attempts You Are now Logged Out Of System")
            
            break

        
    