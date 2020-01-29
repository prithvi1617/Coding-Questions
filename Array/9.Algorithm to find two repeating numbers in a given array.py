
def rep(a,len):
    hmap={}
    for i in range(len):
        if a[i] in hmap:
            hmap[a[i]]+=1
        else:
            hmap[a[i]]=1
    for key in hmap:
        if hmap[key]==2:
            print('repeated no. ',key)




a=[1,2,3,4,5,4,5]
rep(a,len(a))