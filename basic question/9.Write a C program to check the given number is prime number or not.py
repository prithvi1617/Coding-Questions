# divisible by 1 or itself


def prime(n):
    flag=0
    if n==1 or n==2:
        return 'prime'
    else:
        for i in range (2,n//2):
            if(n%i==0):
                flag=1
                break
    
    if flag==1:
        return 'not prime'
    else:
        return 'prime'



n=1
print(prime(n))