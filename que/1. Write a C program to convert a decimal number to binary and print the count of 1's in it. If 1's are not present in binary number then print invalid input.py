

def dtob(n):
    count=0
    while n>0:
        if n%2!=0:
            count+=1
        n=n//2
    return count


n=10
print(dtob(n))