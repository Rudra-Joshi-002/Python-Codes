"""

Question-1: Write a function called factors that takes an integer and returns a list of its factors and how
many factors the number has.
    
"""

def factors(num):
    
    Factor=[]
    
    for i in range(1,num+1):
        
        if num%i==0:
            
            Factor.append(i)
            
    
    nfac=len(Factor)
    
    return Factor,nfac

num=int(input("Enter a Integer Number: "))

Factor=[]

nfac=0

Factor,nfac=factors(num)

print("Factors of ",num," are: ")

print(Factor)

print("Number of Factors of ",num," are: ",nfac)

