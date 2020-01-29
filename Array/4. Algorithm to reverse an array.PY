def rev(a,len):
    l=0
    r=len-1
    for i in range(int(len/2)):
        temp = a[l]
        a[l]= a[r]
        a[r]=temp
        l+=1
        r-=1
    return a
a= [1,2,3,4,5]
print(rev(a,len(a)))

# using recursion
# def rev(a,start,end):
#     if(start>=end):
#         return
#     a[start],a[end] = a[end], a[start] 
#     rev(a,start+1,end-1)


# a= [1,2,3,4,5]
# rev(a,0,4)
# print(a)