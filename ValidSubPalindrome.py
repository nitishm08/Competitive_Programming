def validsubpalindrome(text,left,right):

  while left<=right:

    if text[left]!=text[right]:
      return False

    left+=1
    right-=1

  return True

def almostpalindrome(text):

  i=0
  i2=len(text)-1

  while i <= i2:

    if text[i]!=text[i2]:
      return validsubpalindrome(text,i+1,i2) or validsubpalindrome(text,i,i2-1)

    i+=1
    i2-=1

  return True
