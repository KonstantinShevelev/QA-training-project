def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


primes = [n for n in range(1, 51) if is_prime(n)]
print(primes)
