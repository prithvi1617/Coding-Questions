


def fib(n):
    lis=[0,1]
    for i in range(2,n):
        lis.append(lis[i-1]+lis[i-2])

    for i in range(20):
        print(lis[i])




n=20
fib(n)