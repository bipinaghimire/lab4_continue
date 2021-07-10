'''
Write a Python script to check if a given key already exists in a dictionary.
'''
d={1:'apple', 5:'coconut', 2:'litchi', 4:'mango'}
key= int(input('enter a key to check: '))
print(key in d)