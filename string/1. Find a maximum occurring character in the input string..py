def maxc(str,len):
    max=0
    for i in range(len):
        cur=str.count(str[i])
        if cur>max:
            max=cur
            char=str[i]
    print(max,char)




str='asdsadsvsss'
maxc(str,len(str))