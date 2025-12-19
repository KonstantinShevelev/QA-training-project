def prime_nums(num):
    primes = []
    for i in range(2, num + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes += [i]
    return(primes)


num = int(input("Введи число: "))
print(prime_nums(num))
