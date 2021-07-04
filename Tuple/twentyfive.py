'''
6.Write a Python program to convert a tuple to a string
'''
tup=('a', 'b', 'i', 'e', 'l')
string=''
for i in tup:
    string=string+i
    print(string)
print(type(tup))
print(type(string))
