#Bubble Sort

def bubblesort(nums):

  length=len(nums)-1

  for i in range(length):
    for j in range(length):
      if nums[j]>nums[j+1]:
        temp=nums[j]
        nums[j]=nums[j+1]
        nums[j+1]=temp
      j+=1
    i+=1
  return nums
