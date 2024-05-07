"""

Question-3: Write a function called is_sorted that is given a list and returns True if the list is sorted
and False otherwise

"""

def is_sorted(L):
    
    Lcop=[]
    
    Lcop=sorted(L)
    
    count=0
    
    for i in range(len(L)):
        
        if Lcop[i]==L[i]:
            
            count+=1
            
    if count==len(L):
        
        return True
    
    else:
        
        return False

L=[]

ip=int(input("Enter the number of values you wish to feed: "))

for i in range(ip):
    
    n=int(input("Enter Value: "))
    
    L.append(n)
    

val=0

val=is_sorted(L)

if val:
    
    print("Entered List Is Sorted")
    
else:
    
    print("Entered List Is not Sorted")
            
            
    