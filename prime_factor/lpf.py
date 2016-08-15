def all_factors(n):
    """Get all factors of n."""
    all_fact = []
    for i in range(1, n+1):
        if n % i == 0:
            all_fact.append(i)
    return all_fact

def prime(n):
    """Returns true if n is prime."""
    prime = True
    if n <= 1:
        prime = False
    elif n == 2:
        prime = True
    else:
        for i in range(2, n):
            if n % i == 0:
                prime = False
    return prime

def prime_factors(factors):
    """Returns prime factors within all_factors list."""
    prime_fact = []
    for number in factors:
        if prime(number):
            prime_fact.append(number)
    return prime_fact

def largest_prime_factor(n):
    """Returns largest prime factor for positive integers."""
    try:
        all_fact = all_factors(n)
        prime_fact = prime_factors(all_fact)
        return prime_fact[-1]
    except IndexError:
        print("Largest prime factors of n <= 1 do not exist")
