def binarysearch(nums,left,right,target):

  while left<=right:
    mid= (right+left)//2
    midvalue=nums[mid]
    if target==midvalue:
      return mid
    elif midvalue<target:
      left=mid+1

    else:
      right=mid-1
  
  return -1

def binarysearch2(nums,target):
  if len(nums)<1:
    return [-1,-1]
  firstpos=binarysearch(nums,0,len(nums)-1,target)

  if firstpos==-1:
    return [-1,-1]

  startpos=firstpos
  endpos=firstpos

  while startpos != -1:
    temp1=startpos
    startpos=binarysearch(nums,0,startpos-1,target)

  startpos=temp1

  while endpos != -1:
    temp2=endpos
    endpos=binarysearch(nums,endpos + 1,len(nums)-1,target)

  endpos=temp2
  

  return [startpos,endpos]
