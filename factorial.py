#As simple as the title, given a number N, print the number of digits in N!
#N! is defined as : N! = 1*2*3...(N-1)*N
#0! = 0 and 1! = 1.
#No number ever contains any leading zeros.
#Input Format
#Input contains only one number, N.
#Constraints
#1 <= N <= 1000
#Output Format
#Output one number that is equal to the number of digits in N!
#Sample Input 0
#6
#Sample Output 0
#3

import math 
n=int(input( ))
def finddigits(n):
    if(n<0):
        return 0
    if(n<=1):
        return 1
    digits=0
    for i in range(2,n+1):
        digits += math.log10(i)
    return math.floor(digits)+1;

print(finddigits(n))