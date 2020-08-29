'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def findSmallestMult(num):
    check=1
    while(True):
        totalPos=0
        for i in range(1,num+1):
            if (check%i==0):
                totalPos+=1 
                largest=i;  
        if(totalPos==num):
            return check
        check=largest*((check//largest)+1) #So I dont through every single number


num=20
print(findSmallestMult(num))