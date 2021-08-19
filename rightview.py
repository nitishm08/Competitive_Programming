def dfs(node,currentlevel,result):

  if node==None:
    return

  if currentlevel>=len(result):
    result.append(node.value)

  if node.right:
    dfs(node.right,currentlevel+1,result)

  if node.left:
    dfs(node.left,currentlevel+1,result)

def rightview(rootnode):
  result=[]
  dfs(rootnode,0,result)

  return result

# BFS

def rightview(root):

  if root == None:
    return []
  res=[]
  q=[root]

  while len(q):
    length = len(q)
    count=0
    subarray=[]

    while count < length:

      node=q.pop(0)

      if node.left:
        q.append(node.left)

      if node.right:
        q.append(node.right)

      count +=1

    res.append(node.value)
    
  return res
