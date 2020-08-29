'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

def sumPrimes(num):
    total=0
    if(num<2):
        return 0
    check=2
    for i in range(2,num+1):
        prime=True
        for j in range(2,int(i**(1/2))+1):
            if(i%j==0 and not i==j):
                prime=False
        if(prime):
            total+=i
    return total
    



num=2000000
print(sumPrimes(num))