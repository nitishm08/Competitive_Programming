def cycle(head):

  currentnode=head
  seennodes= {}

  while seennodes.has(currentnode) != True:
    if currentnode.next == None:
      return False

    seennodes.add(currentnode)
    currentnode=currentnode.next
  
  return currentnode

#-------with floyd algorithm -------

def floyd(head):

  turtle=head
  hare= head

  while True:
    hare=hare.next
    turtle=turtle.next
    if hare.next==None or hare==None:
      return False
    hare= hare.next

    if turtle == hare:
      break

  p1=head
  p2=turtle

  while p1 != p2:
    p1=p1.next
    p2= p2.next

  return p1
