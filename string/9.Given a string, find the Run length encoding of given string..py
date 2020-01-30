

def cnt(s):
    l=len(s)
    lis2=[]
    j=1
    for i in range(0,l,2):

        count=1
        while(i<l-1 and s[i]==s[i+1]):
            count+=1
            j+=1
        lis2.append(s[i])
        lis2.append(count)
    print(lis2)



s='aaaabbsssscdddd'
print(cnt(list(s)))