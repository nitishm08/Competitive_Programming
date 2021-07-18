def trappingwater(nums):

  p1=0
  p2=len(nums)-1
  maxleft=0
  maxright=0
  count=0

  while p1<p2:
    if nums[p1]<=nums[p2]:
      maxleft = max(maxleft,nums[p1])
      currentwater= maxleft-nums[p1]
      p1+=1
      if currentwater >0:
        count += currentwater

    elif nums[p1]>nums[p2]:
      maxright= max(maxright,nums[p2])
      currentwater= maxright-nums[p2]
      p2-=1
      if currentwater>0:
        count += currentwater
    
  return count
