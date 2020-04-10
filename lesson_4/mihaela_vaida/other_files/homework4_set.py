set1={1,2,3,4,5,6,7,8,9,10}
set2={11,12,13,14,15,16,17,1,2,10}
print("This is the 1'st set :")
print(set1)
print("This is the second set :")
print(set2)
#union
union_set=set1.union(set2)
print('Union example for set 1 and set2: ' +str(union_set))
#intersection
intersection_set=set1.intersection(set2)
print('Intersection example for set 1 and set2: ' +str(intersection_set))
#difference
difference_set=set1.difference(set2)
print('Differention example for set 1 and set2: ' +str(difference_set))
#symetric difference.
symetric_difference_set=set1.symmetric_difference(set2)
print('Symetric Differention example for set 1 and set2: ' +str(symetric_difference_set))