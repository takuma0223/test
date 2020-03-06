n, i = int(input()), 2
while i <= n ** (1/2):
    if n % i == 0:
        print('not sosu')
        break
    i += 1
else:
    print('sosu')