'''
10.Write a Python program to sum all the items in a dictionary.
'''
sum=0
d={1:2,2:4,3:6,4:8,5:10}
for i in d.values():
    sum=sum+i
print(f'The sum of items of dictionary is {sum}')