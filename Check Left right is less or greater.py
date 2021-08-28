def dfs(root,min,max):
  if node.value <= min or node.value>=max:
    return False

  if node.left:
    if dfs(node.left,min,node.value) == False:
      return False

  if node.right:
    if dfs(node.right,node.value,max) == False:
      return False

  return True

def valid(root):
  if root != None:
    return True
  
  return dfs(root,float('-inf'),float('inf'))
