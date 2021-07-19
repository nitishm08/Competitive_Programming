#Solution 1

def typedout(S,T):

  nums1=[]
  nums2=[]

  for x in S:
      try:
          if x=='#':
              nums1.pop()
          else:
              nums1.append(x)
      except:
          pass
  for x in T:
      try:
          if x=='#':
              nums2.pop()
          else:
              nums2.append(x)
      except:
          pass

  if nums1==nums2:
      return True
  else:
      return False
    
    
#Solution 2 (might not work in some cases)

def typedout(S,T):

  s1=len(S)-1
  t1=len(T)-1

  while s1>=0 or t1>=0:
    if S[s1]=='#' or T[t1]=="#":
      if s1>=0 and S[s1]=="#":
        backcount=2

        while backcount>0:
          s1-=1
          backcount-=1

          if S[s1]=="#" and s1>=0:
            backcount+=2

      elif t1>=0 and T[t1]=="#":
        backcount=2

        while backcount>0:
          t1-=1
          backcount-=1

          if T[t1]=="#" and t1>=0:
            backcount+=2

    else:
      if S[s1]!=T[t1]:
        return False
      else:
        s1-=1
        t1-=1
  return True
