def sumtwo(nums,target):
  number={}

  for p1 in range(len(nums)):
    try:
      currentnum=number[nums[p1]]

      if currentnum>=0:
        return currentnum,p1
    except:
      targetnum=target-nums[p1]
      number[targetnum]=p1
