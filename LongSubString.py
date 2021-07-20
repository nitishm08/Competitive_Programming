#Brute Force solution

def longsubstring(text):

  string= []
  count=0
  p=0

  for i in range(len(text)):
    if text[i] not in string:
      string.append(text[i])
      count=max(len(string),count)
      i+=1
    else:
      p+=1
      i=p
      string=[]

  return count

#optimal Solution

def longsubstring(text):

  if len(text)<=1:
    return len(text)

  n=len(text)
  map={}
  i=0
  ans=0

  for p in range(n):
    if text[p] in map:
      i=max(i,map[text[p]])

    ans=max(ans,p-i +1)
    map[text[p]]=p+1

  return ans
