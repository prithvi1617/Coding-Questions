

def fin(str1,pat):
    ls=len(str1)
    lp=len(pat)
    print(ls-lp+1)

    for i in range(ls-lp+1):
        j=0
        for k in range(lp):
            if str1[i+k]!=pat[k]:
                break
            j+=1
        
        if (j==lp):
            print('pattern found at',i)






str1='aabaaaaabakjujnaabaklmkhaabajijaojabaabojaaba'
pat='aaba'


fin(str1,pat)