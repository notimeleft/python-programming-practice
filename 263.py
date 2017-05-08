#Write a program to check whether a given number is an ugly number.

#Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

#Note that 1 is typically treated as an ugly number.
import math
'''
def check_prime(k):
    for i in range(2,k):
        if k%i==0:
            return False
    return True
def factors(n):
    return set(reduce(list.__add__,
                ([i, n/i] for i in range(2, int(n**0.5) + 1) if n % i == 0 and check_prime(i))))

def check_list(set_f):
    for k in set_f:
        if not check_prime(k):
            set_f.remove(k)
    return set_f
'''
def isUgly(num):
    if(num==1 ):
            return True
    if(num<=0):
        return False
    beaut = [2,3,5]
    factors = []
    for i in range(2,int(math.sqrt(num))):
        if num%i==0 and check_prime(i):
            factors.extend([i,num/i])

    print beaut, factors
    k = set(factors)-set(beaut)
    print k
    if len(k)>0:
        return False
    return True


def check_prime(k):
    for i in range(2,int(math.sqrt(k))):
        if k%i==0:
            return False
    return True

print isUgly(7)

#print check_prime(372677233)
