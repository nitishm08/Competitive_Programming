#Kth element

def swap(array,i,j):
  temp=array[i]
  array[i]=array[j]
  array[j]=temp

def getPartition(nums,left,right):
  pivotElement=nums[right]
  partitionIdx=left

  j= left

  while j<right:
    if nums[j]<=pivotElement:
      swap(nums,partitionIdx,j)
      partitionIdx+=1
    j+=1

  swap(nums,partitionIdx,right)

  return partitionIdx

def quickselect(nums,left,right,indexTofind):

  if left<right:
    partitionIdx=getPartition(nums,left,right)
    if partitionIdx==indexTofind:
      return nums[partitionIdx]

    elif indexTofind<partitionIdx:
      return quickselect(nums,left,partitionIdx-1,indexTofind)

    else:
      return quick(nums,partitionIdx+1,right,indexTofind)

def findKthLargest(nums,k):
  indexTofind=len(nums)-k
  quicksort(nums,0,len(nums)-1)

  return nums[indexTofind]
