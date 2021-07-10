'''
Write a Python script to generate and print a dictionary that contains a number (between 1 and n)
in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
'''
n=int(input('enter your range:'))
d={x:x*x for x in range(1,n)}
print(d)
d2={x:x*x for x in range(1,n) if x%2==1}
print(d2)
d3={x:x*x for x in range(1,n) if x%2==0}
print(d3)