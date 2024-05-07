"""

Question-4: Write a program that gets a string from the user containing a potential telephone number.
The program should print Valid if it decides the phone number is a real phone number, and
Invalid otherwise. A phone number is considered valid as long as it is written in the form
abc-def-hijk or I-abc-def-hijk. The dashes must be included, the phone number should contain
only numbers and dashes, and the number of digits in each group must be correct. Test your
program with the output shown below.
Enter a phone number: 1-301-447-5820
Valid
Enter a phone number: 301-447-5820
Valid
Enter a phone number: 301-4477-5820
Invalid
Enter a phone number: 3X1-447-5820
Invalid
Enter a phone number: 3014475820
Invalid

"""

tele=input("Enter your phone number: ")

if len(tele)==12 or len(tele)==14:
    
    if len(tele)==12:
            
        if tele[3]=="-" and tele[7]=="-":
            
            tele1=tele[0:3]
            
            tele2=tele[4:7]
            
            tele3=tele[8:12]
            
            if tele1.isdigit() and tele2.isdigit() and tele3.isdigit():
                
                print("Valid Number")
                
            else:
                
                print("Invalid Number")
    
    
        else:
                
            print("Invalid Number")
            
    elif len(tele)==14:
        
        if tele[1]=="-" and tele[5]=="-" and tele[9]=="-":
            
            tele1=tele[0:1]
            
            tele2=tele[2:5]
            
            tele3=tele[6:9]
            
            tele4=tele[10:14]
            
            if tele1.isdigit() and tele2.isdigit() and tele3.isdigit() and tele4.isdigit():
                
                print("Valid Number")
                
            else:
                
                print("Invalid Number")
                
        else:
            
            print("Invalid Number")
            
else: 
   
    print("Invalid Number")
            
            
            
            
            
    
            
                
                
                