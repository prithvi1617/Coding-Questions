
def maxDiff(a,len):
    a.sort()
    diff=a[len-1]-a[0]
    return diff



arr = [1, 2, 90, 10, 110] 

size = len(arr) 
print ("Maximum difference is", maxDiff(arr, size))