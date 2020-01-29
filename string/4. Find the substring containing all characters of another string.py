
def substr(str1,str2,len1,len2):
    if len1>=len2:
        for i in range(len1):
            k=i
            count=0
            for j in range(len2):
                if(str1[k]!=str2[j]):
                    break
                k+=1
                count+=1
            if count==len2:
                return 'string found'
    return 'not found'


str1='abcdef'
str2='abc'
print(substr(str1,str2,len(str1),len(str2)))