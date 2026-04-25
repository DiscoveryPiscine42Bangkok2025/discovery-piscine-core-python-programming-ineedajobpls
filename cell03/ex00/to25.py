n = int(input('enter a number less than 25: '))

if n > 25:
    print('error')
else:
    while n <= 25:
        print('inside the loop my variable is', n )
        n += 1