# def dup(lis):
#     s=set()
#     for i in lis:
#         s.add(i)
#     str1=''.join(s)
#     print(s)
#     print(str1)

# def dup1(lis):
#     l=len(lis)

#     dict={}
#     for i in range(l):
#         dict[lis[i]]=1
#     key=dict.keys()
#     return(''.join(key))

# # Driver program 
# s1 = "geeksforgeeg"

# print(dup1(list(s1)))






def dup1(lis):
    lis2=[]
    for i in lis:
        if(i not in lis2):
            lis2.append(i)
    return ''.join(lis2)


# Driver program 
s1 = "geeksforgeeg"

print(dup1(list(s1)))