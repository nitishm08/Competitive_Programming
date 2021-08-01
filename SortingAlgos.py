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

#Selection Sort

def selectionsort(nums):

  length=len(nums)-1

  for i in range(length):
    minnumber=i
    j=i+1
    temp=nums[i]
    while j<= length:
      if nums[j]<nums[minnumber]:
        minnumber=j
      j+=1
    nums[i]=nums[minnumber]
    nums[minnumber]=temp
    i+=1

  return nums

#Insertion Sort

def insertionsort(nums):

  for i in range(1,len(nums)):
    temp=nums[i]

    j=i-1

    while j>=0 and temp <nums[j]:
      nums[j+1]=nums[j]
      j-=1

    nums[j+1]=temp

  return nums
