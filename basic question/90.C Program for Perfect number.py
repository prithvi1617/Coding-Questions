


def perfect(n):
    count=1
    for i in range(2,n//2+1):
        if (n%i==0):
            count+=i
    if count==n:
        return 'yes'
    else:
        return 'no'

n=6
print(perfect(n))