def uniqeprime(n):
    if n is None or n<=1:
        return []
    factors=[]
    #factors of 2s
    if n%2==0:
        factors.append(2)
    while n%2==0:
        n//=2
    #factor out odd primes
    p=3
    while p*p<=n: #(We only need to check factors up to √n,Example: For n=60, √60 ≈ 7.74 → we only check 3, 5, 7.)
     if n%p==0:
        factors.append(p)
        while n%p==0:
         n//=p
     p+=2
#if reminder is prime
    if n>1:
     factors.append(n)
    return factors    
# quick tests
print(uniqeprime(60))  # [2, 3, 5]
print(uniqeprime(84))  # [2, 3, 7]
print(uniqeprime(97))  # [97]
print(uniqeprime(1))   # []