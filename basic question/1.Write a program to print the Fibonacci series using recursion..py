

def fib(n):
    fib1=0
    if n==1:
        return 0
    if n==2:
        return 1
    fib1=fib(n-1)+fib(n-2)
    return(fib1)





no=5
print(fib(no))