
def fact(no):
    fact=1
    for i in range(no,0,-1):
        fact*=i
        
    return fact

no=5
print(fact(no))