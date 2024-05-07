"""

Question-2: Write a function called matches that takes two strings as arguments and returns how many
matches there are between the strings. A match is where the two strings have the same character at the same index. 
For instance, 'python' and 'path' match in the first, third, and fourth characters, so the function should return 3

"""

def matches(str1,str2):
    
    len1=len(str1)
    
    len2=len(str2)
    
    count=0
    
    for i  in range(min(len1, len2)):
        
        if str1[i]==str2[i]:
            
            count+=1
            
    
    return count

str1=input("Enter A String: ")

str2=input("Enter Another String: ")

cchar=matches(str1, str2)

print("Entered Strings Are: ")

print("STR1: ",str1)

print("STR2: ",str2)

print("Number of common characters between the two strings are: ",cchar)