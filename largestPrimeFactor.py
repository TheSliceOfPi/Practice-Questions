'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def getLargestPrimeFactor(num):
    maxPr=-1
    n=num
    while(n%2==0):
        maxPr=2
        n=n//2
    check=3
    while(check<=(n**(1/2))):
        if(n%check==0):
            maxPr=check
            n=n/check
        check+=1
    if(n>2):
        maxPr=n
    return int(maxPr)


num=600851475143
print(getLargestPrimeFactor(num))