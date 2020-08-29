'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''


def getNthPrime(n):
    num=0
    prime=2
    while(True):
        boolPrime=True
        for i in range(2,int(prime**(1/2))+1):
            if(prime%i==0):
                boolPrime=False
        if(boolPrime):
            num+=1
        if(num==n):
            return prime
        prime+=1
        



n=10001
print(getNthPrime(n))