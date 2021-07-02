n = 1260
coin_list = [500, 100, 50, 10]
count = 0

for coin in coin_list:
    count += n//coin
    n %= coin
print(count)
