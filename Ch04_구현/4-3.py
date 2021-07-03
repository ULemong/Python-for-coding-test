n = input()

count = 0
a = ord(n[0])
x = a - 96 #'a'의 값이 97이기 때문

j = 2
for i in range(1,3):
    if i == 2:
        j = 1
    if (x+i) < 9:
        if int(n[1])+j < 9:
            count += 1
        if int(n[1])-j > 0:
            count += 1
    if int(x-i) > 0:
        if int(n[1])+j < 9:
            count += 1
        if int(n[1])-j > 0:
            count += 1
    else:
        continue

print(count)