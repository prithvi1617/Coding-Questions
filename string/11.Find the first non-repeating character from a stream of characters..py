
def ch(s,len):
    m={}
    for i in range(len):
        if s[i] in m:
            m[s[i]]+=1
        else:
            m[s[i]]=1
    
    for key in m:
        if m[key]==1:
            return key
    



s='qqqqwwwweerwwsss'
print(ch(s,len(s)))