"""
Create two sets with 10 numbers each (some of the numbers should be present in both sets). With these two sets,
exemplify the following basic sets operations: union, intersection, difference and symmetric difference.
"""

# create set 1
set1 = {1, 2, 3, 4, 5, 6, 3, 2, 7, 8, 9, 10}

print(set1)  # everything has to be unique
print('  ')  # empty line

# create set 2
set2 = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}

print(set2)  # everything has to be unique
print('  ')  # empty line

# union - unite uniques elements between two sets
print(set1.union(set2))
print('  ')  # empty line

# intersection - common values between two sets
print(set1.intersection(set2))
print('  ')  # empty line

# difference - difference between two sets
print(set1.difference(set2))  # what set1 has different compared with set2?
print(set2.difference(set1))  # what set has different compared with set1?
print('  ')  # empty line

#  symmetric difference
print(set1.symmetric_difference(set2))  # remove common elements between sets and shows only whats are differences
print('  ')  # empty line

'''
create 2 sets: one smaller that contains few numbers of set2 and one larger that contain every number from both sets
'''

set3 = {5, 6, 7}
set4 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

# issubset - test whether every element in the set is in other - return boolean
print(set3.issubset(set1))  # True
print(set3.issubset(set2))  # True
print('  ')  # empty line

# issuperset  - Test whether every element in other is in the set
print(set4.issuperset(set1))  # True
print(set1.issuperset(set4))  # False
