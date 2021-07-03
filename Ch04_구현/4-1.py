n = int(input())
plan = input().split()
x, y = 1, 1

for i in plan:
    if i == 'R':
        if y == n:
            continue
        y += 1
    elif i == 'L':
        if y == 1:
            continue
        y -= 1
    elif i == 'U':
        if x == 1:
            continue
        x -= 1
    else:
        if x == n:
            continue
        x += 1

print(x, y)