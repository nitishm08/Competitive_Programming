def mostwater(nums):
  maxarea=0
  i=0
  i2= len(nums)-1
  while i<i2:
    b=i2-i
    l=min(nums[i],nums[i2])
    area=l*b
    maxarea= max(area,maxarea)

    if nums[i]<=nums[i2]:
      i+=1
    else:
      i2-=1
  return maxarea
