def reverse(head):

  prevnode=None
  currentnode=head

  while currentnode:
    next=currentnode.next
    currentnode.next=prevnode
    prevnode=currentnode
    currentnode=next

  return prevnode
