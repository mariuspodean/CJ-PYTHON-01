
#Missing methods: Two list methods are not listed here. Using the python documentation
#find out the missing methods and play with then to figure out what

# 1. Index
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.index('banana')
fruits.index('banana', 5)  # Find next banana starting a position 5

# 2. Count
fruits.count('orange')  #1
fruits.count('banana')  #2

#3. Sort

fruits.sort()
fruits    #['apple', 'apple', 'banana', 'banana', 'kiwi', 'orange', 'pear']

#4.  Reverse

fruits.reverse()
fruits  #['pear', 'orange', 'kiwi', 'banana', 'banana', 'apple', 'apple']

#5. Copy

basket=fruits.copy()
basket   #['pear', 'orange', 'kiwi', 'banana', 'banana', 'apple', 'apple']

#. Popleft() 
from collections import deque
basket_=deque(['pear', 'orange', 'kiwi', 'banana', 'banana', 'apple', 'apple'])
basket_.popleft()
#'pear'
