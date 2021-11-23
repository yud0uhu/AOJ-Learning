n = int(input())
R = [int(input()) for _ in range(n)]

minv = R[0]
maxv = -2000000000;

for i in range(1,n):
    maxv = max(maxv, R[i]-minv)
    minv = min(minv, R[i])

print(maxv)
