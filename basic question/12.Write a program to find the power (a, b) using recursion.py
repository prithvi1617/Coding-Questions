

def power(a,b):
    val=1
    if b==0:
        return 1
    val=power(a,b-1)*a
    return val


a=2 
b=0
print(power(a,b))