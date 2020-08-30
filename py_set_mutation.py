nt(input())
s = set(map(int, input().split()))
N = int(input())

for i in range(N):
    S = input().split()
    if S[0] == "intersection_update":
        s.intersection_update(set(map(int, input().split())))
    elif S[0] == "update":
        s.update(set(map(int, input().split())))
    elif S[0] == "symmetric_difference_update":
        s.symmetric_difference_update(set(map(int, input().split())))
    elif S[0] == "difference_update":
        s.difference_update(set(map(int, input().split())))

print(sum(s))
