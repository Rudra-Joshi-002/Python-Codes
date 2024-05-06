"""
Question-1: A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years
unless they are also divisible by 400. Ask the user to enter a year, and, using the // operator,
determine how many leap years there have been between 1600 and that year.

"""

year=int(input("Enter a Year after 1600: "))

count=1

for i in range(1600,year,1):
    
    if i%4==0:
        
        if i%100==0:
            
            if i%400==0:
                
                count+=1
        
        elif i%100!=0:
            
            count+=1
        
        
print("Number of Leap Years Between 1600 and ",year," Is ",count)

    
    