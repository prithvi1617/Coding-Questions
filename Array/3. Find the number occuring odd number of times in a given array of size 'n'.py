# using hashing
# def number(a,len):
#     hmap = {}

#     for i in range(len):
#         if a[i] in hmap:
#             hmap[a[i]]+=1
#         else:
#             hmap[a[i]]=1
#     count=0
#     for key in hmap:
#         if hmap[key]%2!=0:
#             count=1
#             k=key
#     if count==1:
#          print('element found',k)
#     else:
#         print('element not found')


#using XOR

def number(a,len):
    value=0
    for i in range(len):
        value=value^a[i]
    if value==0:
        print('element not found')    
    else:
        print('element found',value)

a = [1,2,3,4,5,5,4,3,2]
number(a,len(a))