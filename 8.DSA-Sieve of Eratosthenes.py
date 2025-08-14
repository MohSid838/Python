def sieveof_eratosthenes(n):
    isprime=[True] * (n+1)
    primes=[]
    
    for i in range(2, int(n**0.5)+1):
        if isprime[i]:
            for j in range(i*i,n+1,i):
                isprime[j]=False
    for i in range(2,n+1):
        if isprime[i]:
            primes.append(i)
    return primes
print(sieveof_eratosthenes(30))
