def reversebetween(head,m,n):

  currentnode=head
  start=head
  current_position=1

  while current_position<m:
    start=currentnode
    currentnode=currentnode.next
    current_position +=1

  newlist=None
  tail=currentnode

  while current_position>=m and current_position <=n:
    next=currentnode.next
    currentnode.next= newlist
    newlist= currentnode
    currentnode= next
    current_position+=1

  start.next= newlist
  tail.next=currentnode

  if m>1:
    return head
  else:
    newlist
