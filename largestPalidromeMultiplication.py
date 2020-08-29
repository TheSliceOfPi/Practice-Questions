'''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def checkLargestPali(numStr):
    starter=10**(num)-1
    temp=starter*starter
    for i in range(starter,0,-1):
        for j in range(starter,0,-1):
            temp=str(i*j)
            lenTemp=len(temp)
            if(lenTemp%2==0 and temp[:lenTemp//2]==temp[-1:lenTemp//2-1:-1]):
                return temp
            elif(lenTemp%2==1 and temp[:lenTemp//2]==temp[-1:lenTemp//2:-1]):
                return temp




num=3
print(checkLargestPali(num))