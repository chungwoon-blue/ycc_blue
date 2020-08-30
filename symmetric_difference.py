M = int(input())
m = input().split()
N = int(input())
n = input().split()

m1 = set(map(int, m))
n1 = set(map(int, n))
s = m1 ^ n1
s1 = sorted(list(s))
for i in s1:
        print(i)
        
