

def rev(no,len):
    l=0
    r=len-1
    for i in range(int(len/2)):
        no[l],no[r]=no[r],no[l]
        l+=1
        r-=1
    return ''.join(no)


no='123456'
print(rev(list(no),len(no)))