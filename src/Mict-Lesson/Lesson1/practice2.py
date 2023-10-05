def is_prime(n):
    if not isinstance(n, int):
        return False
    elif n < 2:
        return False
    for m in range(2, n//2+1):
        if n % m == 0:
            return False
    return True

def prime_number(x):
    ans = 0
    for i in range(0,x+1):
        if is_prime(i):
            ans += 1
    return ans

def prime_number_sum(x):
    ans = 0
    for i in range(0,x+1):
        if is_prime(i):
            ans += i
    return ans

print("100までの素数の数は",prime_number(100))
print("100までの素数の総和は",prime_number_sum(100))
