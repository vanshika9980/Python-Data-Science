import sys

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

prime_sum = 0

for num in sys.argv[1:]:
    n = int(num)

    if is_prime(n):
        prime_sum += n

print("Sum of prime numbers =", prime_sum)