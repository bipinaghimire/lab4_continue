'''
Write a Python program to remove an item from a set if it is present in the set.
'''
s={1,3,5,7}
a =int(input('enter an item from set to discard: '))
s.discard(a)
print(s)