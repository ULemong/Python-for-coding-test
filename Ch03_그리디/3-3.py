#min()함수 이용#
n, m = map(int, input().split())
b = []

for i in range(n):
    a = list(map(int, input().split()))
    s = min(a)
    b.append(s)

print(max(b))

#이중 for문 이용#
n, m = map(int, input().split())
b = []

for i in range(n):
    a = list(map(int, input().split()))
    s = a[0]
    for j in range(m):
        if a[j] < s:
            s = a[j]
    b.append(s)

print(max(b))
