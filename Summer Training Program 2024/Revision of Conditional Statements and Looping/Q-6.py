"""
Question-6: Write a function that swaps the values of three variables x, y, and z, so that x gets the value
of y, y gets the value of z, and z gets the value of x.
"""

def swap(x,y,z):
    
    temp=x
    
    x=y
    
    y=temp
    
    temp=z
    
    z=y
    
    y=temp
    
    return x,y,z

x=float(input("Enter any value: "))

y=float(input("Enter any value: "))

z=float(input("Enter any value: "))

print("Before Swapping x,= ",x," y= ",y," z= ",z)

x,y,z=swap(x, y, z)

print("After Swapping x,= ",x," y= ",y," z= ",z)