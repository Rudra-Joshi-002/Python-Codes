# -*- coding: utf-8 -*-
"""
Question-1: Given a list L = [2,2,3,5,2,6,39,42,32,42,5,39,64,42].
(i) create a new list whose first element is how many 2 s are in L whose second element is how
many other numbers are there in L, etc.(means it finds frequency of each aumber present in L)
(Hint.: use count method of list)
(ii) Write a program that prints out the two largest and two smallest elements of a list L.

"""

L=[2,2,3,5,2,6,39,42,32,42,5,39,64,42]

count2s=0

countothers=0

for i in range(len(L)):
    
    if L[i]==2:
        
        count2s+=1
        
    else:
        
        countothers+=1


LR=[0,0]

LR[0]=count2s

LR[1]=countothers

print("List L is Given As: ",L)

print("List whose 1st ELement Shows Number of 2's In Above list and whose 2nd Element Shows Number of Other Elements Irrespective of recursion is: ",LR)    

Lcop=sorted(L)

smallest1=min(L)

Largest1=max(L)

smallest2=0

Largest2=0

for i in range(len(L)):
    
    if Lcop[i]>smallest1:
        
        smallest2=Lcop[i]
        
        break
    
for i in range(len(L)):
    
    if Lcop[len(L)-i-1]<Largest1:
        
        Largest2=Lcop[len(L)-i-1]
        
        break
    
print("Two Smallest Numbers In List Are: ",smallest1," ,",smallest2)

print("Two Largest Numbers In List Are: ",Largest1," ,",Largest2)