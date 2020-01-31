

def fact(no):
    fact1=1
    if no==1:
        return 1
    fact1=fact(no-1)*no
    print(fact1)
    return fact1


no=5
print(fact(no))