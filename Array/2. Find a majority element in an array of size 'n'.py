# def majority(a,len):
#     appear = int(len/2)

#     for i in range(appear):
#         count=0
#         for j in range(len):
#             if a[i] == a[j]:
#                 count+=1
#         if (count >=appear):
#             print('element found',a[i])
#             break


def majority(a, len):
    hashMap = {}
    for i in range(len):
        if a[i] in hashMap:
            hashMap[a[i]]+=1
        else:
            hashMap[a[i]]=1
    count=0
    for key in hashMap:
        if hashMap[key] > len/2:
            count=1
            break
    if count == 1:    
        print('element found',key) 
    
    else:
        print('element not found')



a= [2,2,2,3,3,4,3,3,3,3,3,3]
majority(a,len(a))