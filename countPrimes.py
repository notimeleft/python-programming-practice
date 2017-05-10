#Count the number of prime numbers less than a non-negative number, n.

from math import sqrt
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        #employ a sieve to check off potential primes from a list of 1's representing prime number at index i. 

        primes = [0,1]+[1]*(n-2)
        for i in xrange(2,n):
            if primes[i]==1:
                for x in xrange(2*i,n,i):
                    primes[x]=0
        count=-1
        for x in primes:
            if x==1:
                count+=1
        return count        
    
    
    #isn't used in this solution, but if we're checking whether a single number is prime, we can check from 2 to the square root of the number to reduce computation
    def isPrime(self,n):
        k = int(sqrt(n))
        for i in xrange(2,k+1):
            if n%i==0:
                return False
        return True