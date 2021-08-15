def maxdepth(node,count):

  if node==None:
    return 0

  count+=1

  return max(maxdepth(node.left,count),maxdepth(node.right,count))
