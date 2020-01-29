# O(n*d)
def rotate(a,len,d):
    l=0
    r=len-1
    for i in range(d):
        temp=a[0]
        for j in range(len-1):
            a[j]=a[j+1]
        a[r]=temp
    print(a)


a= [1,2,3,4,5]
d=3
rotate(a,len(a),d)