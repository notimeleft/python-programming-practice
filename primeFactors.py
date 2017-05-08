

def prime_factors(n):
    original_n = n
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            if i not in factors:
            	factors.append(i)
    if n > 1 and original_n!=n:
        factors.append(n)
    return factors


print prime_factors(10001)    