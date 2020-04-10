# Using the python documentation find out the missing methods and play with them to figure out what they do.
# Write code snippets for each method proving the usefulness of the methods.


# list.sort()

numbers = [10, 15, 3, 5]

print(numbers)

numbers.sort()
print(numbers)

# list.reverse()

numbers.reverse()
print(numbers)

# list.index()
index = numbers.index(10)
print('The index of number 10 is:', index)

# list.count() this method will return an iteger value, the count of the given element from the given list.
# It returns a 0 if the value is not found in the given list
numbers_count = numbers.count(9)
print('The count of number 9 is: ', numbers_count)

numbers_count = numbers.count(3)
print('The count of number 3 is: ', numbers_count)

# list.copy

new_numbers = numbers.copy()
print("Old numbers: ", numbers)
print("New numbers: ", new_numbers)
