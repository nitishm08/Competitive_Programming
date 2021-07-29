def validparentheses(text):

  params={"[":"]","(":")","{":"}"}

  if len(text)==0:
    return True

  box=[]

  for i in range(len(text)):
    if text[i] in params.keys():
      box.append(text[i])
    elif params[box.pop()]!=text[i]:
      return False

  return len(box)==0
