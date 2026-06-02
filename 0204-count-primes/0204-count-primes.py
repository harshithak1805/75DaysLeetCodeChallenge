class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        primes=[True]*n
        primes[0]=primes[1]=False
        p=2
        while p**2 <n:
            if primes[p]:
                for i in range(p*p,n,p):
                    primes[i]=False
            p+=1
        return sum(primes)