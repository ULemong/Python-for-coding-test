#스스로 작성한 코드#
n, m, k = map(int, input().split())
a = list(map(int, input().split()))
sum = 0
count = 0

for i in range(m):
    count += 1
    if count%(k+1) == 0:
        # 가장 큰 수 b에 저장
        b = max(a)
        a.remove(max(a))
        # 두 번째로 큰 수
        sum += max(a)
        # a에 b값 다시 추가
        a.append(b)
        continue
    sum += max(a)
print(sum)

#한 번 읽고 작성한 코드#
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

first = data[n-1]
second = data[n-2]

a = first * (k * (m/(k+1)))
a = a + (m % (k+1))

b = second * (m/(k+1))

print(int(a+b))

#정답 코드#
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

#여기서 count값을 미리 계산하면 second값을 계산할 때 연산을 줄일 수 있다
count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)