def removebracket(text):

  if len(text)==0:
    return text

  box=[]
  newstring=list(text)

  for i in range(len(newstring)):
    if newstring[i]=="(":
      box.append(i)
    elif newstring[i]==")" and len(box):
      box.pop()

    elif newstring[i]==")":
      newstring[i]=""
      
  while len(box) !=0:
    index=box.pop()
    newstring[index]=""

  return "".join(newstring)
