"""
Question-2: Generate a random number between 1 and 10. Ask the user to guess the number and print a
message based on whether they get it right or not.
"""
import numpy as np

num=np.random.randint(1,10)

usnum=int(input("Guess A Integer Number Between 1 to 10: "))

if usnum==num:
    
    print("Your Guess is Correct")
    
else:
    
    print("Your Guess is Incorrect")
    
print("The Actual Number Generated By System: ",num)