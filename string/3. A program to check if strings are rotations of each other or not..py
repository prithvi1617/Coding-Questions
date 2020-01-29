

def comp(str1,str2,len1,len2):
    if len1==len2:
        l=0
        r=len1-1
        count=0
        for i in range(len1):
            if(str1[l]!=str2[r]):
                count=1
            l+=1
            r-=1
        if(count==1):
            return 'no'
        else:
            return 'yes'
    return 'no'

str1 = 'abcde'
str2 = 'edcba'
print(comp(str1,str2,len(str1),len(str2)))