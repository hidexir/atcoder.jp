n = input()
isPrime = int(n)%2
tmp = int(n)//2

if isPrime == 0:
    print(tmp)
else:
    print(tmp+1)