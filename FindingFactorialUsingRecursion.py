def factorial(x):

  if x<=1:
    return 1

  else:
    return x*factorial(x-1)

# Tail Recursion  
  
def tailfactorial(x,total=1):
  if x==0:
    return total

  else:
    return tailfactorial(x-1,total*x)
