'''Create two sets with 10 numbers each (some of the numbers should be present in both sets). With
these two sets, exemplify the following basic sets operations: union, intersection, difference and
symetric difference.
'''
A={0,2,4,6,7,8,9,10,12,14}
len(A)
B={0,1,-2,3,4,8,9,11,14,15}
len(B)
print('A=', A)
print('B=',B)
#Union
Union=A|B
print('Union= ', Union)

#Intersection
Intersection=A&B
print('Intersection= ',Intersection)

#Difference
print('A-B=',A-B)
print('B-A=',B-A)

#Symetric Difference
 
print('A^B=',A^B)

print('B^A', B^A)

A^B==B^A
#True
