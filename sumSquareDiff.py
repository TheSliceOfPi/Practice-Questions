'''
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''


def sumSqrDiff(num):
    add=0
    sqr=0
    for i in range(1,num+1):
        add+=i**2
        sqr+=i

    sqr=sqr**2
    diff=sqr-add
    return diff


num=100
print(sumSqrDiff(num))