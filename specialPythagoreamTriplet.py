'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

def getPythTriplet(num):
    for a in range(num):
        for b in range(num//3+1):
            c=((a**2)+(b**2))**(1/2)
            if(a+b+c==num):
                return int(a*b*c)


num=1000
print(getPythTriplet(num))