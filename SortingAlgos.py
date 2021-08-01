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

#MERGE SORT

import math
def mergesort(nums):

  if len(nums)==1:
    return nums

  length=len(nums)
  middle=math.floor(length/2)
  left=nums[0:middle]
  right=nums[middle:]

  return merge(
      mergesort(left),
      mergesort(right)
  )

def merge(left,right):
  result=[]
  leftindex=0
  rightindex=0

  while leftindex<len(left) and rightindex<len(right):
    if left[leftindex]<right[rightindex]:
      result.append(left[leftindex])
      leftindex+=1

    else:
      result.append(right[rightindex])
      rightindex+=1

  return result + left[leftindex:] + right[rightindex:]
