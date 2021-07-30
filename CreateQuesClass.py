class createques():

  def __init__(self):
    self.enter=[]
    self.out=[]

  def enqueue(self,val):
    self.enter.append(val)

  def dequeue(self):
    if len(self.out)==0:
      while len(self.enter):
        self.out.append(self.enter.pop())

    return self.out.pop()

  def peek(self):
    if len(self.out)==0:
      while len(self.enter):
        self.out.append(self.enter.pop())

    return self.out[len(self.out)-1]

  def empty(self):
    return len(self.enter)==0 and len(self.out)==0
