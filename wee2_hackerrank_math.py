#https://www.hackerrank.com/challenges/polar-coordinates/problem

import cmath 
z = input()
print (abs(complex(z)))
print (cmath.phase(complex(z)))

#https://www.hackerrank.com/challenges/python-mod-divmod/problem
a = int(input())
b = int(input())

print (a // b)
print (a % b)
print ( (a // b, a % b))

#https://www.hackerrank.com/challenges/python-power-mod-power/problem
a = int(input())
b = int(input())
c = int(input())

print ( a ** b )
print (pow(a,b,c))

#https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem
a = int(input())
b = int(input())
c = int(input())
d = int(input())

print ((a ** b) + (c ** d))
