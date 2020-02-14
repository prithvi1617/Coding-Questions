# Given a number x, determine whether the given number is Armstrong number or not. A positive integer of n digits is called an Armstrong number of order n (order is number of digits) if.

# abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + .... 
# Example:

# Input : 153
# Output : Yes
# 153 is an Armstrong number.
# 1*1*1 + 5*5*5 + 3*3*3 = 153
def arm(n):
    sum=0
    num=n
    while(n>0):
        val=n%10
        sum+=val*val*val
        n=int(n/10)
    
    if sum==num:
        return 'yes armstrong'
    else:
        return 'n0'



n=153
print(arm(n))





