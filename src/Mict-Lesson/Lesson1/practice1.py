print("Hello World!")

t = 2
for n in [3,5,7,11,13,17,19]:
    t = t + n
print(t)

t = 0
for n in range(0,100,1):
    t = t + n
print(t)

def factoral(n):
    f = 1
    for m in range(2, n+1):
        f = f * m
    return f
print("Factoral of 10 is", factoral(10))

def is_prime(n):
    if not isinstance(n, int):
        return False
    elif n < 2:
        return False
    for m in range(2, n//2+1):
        if n % m == 0:
            return False
    return True
print(is_prime(19))
print(is_prime(20))