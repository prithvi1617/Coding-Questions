

def rem(a,len):
  dict={}
  y=''
  for i in range(len):
      dict[a[i]]=1
  for key in dict:
      y=y+key
    
  print (y)
  


a='geeksforgeeks'
rem(a,len(a))