

def pall(str1,len):
    l=0
    r=len-1
    flag=0
    for i in range(len):
        if str1[l]!=str1[r]:
            flag=1
            break
        l+=1
        r-=1
    if flag==1:
        return 'no'
    else:
        return 'yes'



str1='abcdeddcba'
print(pall(list(str1),len(str1)))