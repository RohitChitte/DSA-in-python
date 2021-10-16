# Recursion.

def sum(n):
    if n == 0:
        return 0
    elif n ==  1:
        return 1
    else:
        return n+sum(n-1)

def fib(n):
    if n==0 or n==1:
        return n 
    else :
        return  fib(n-1)+fib(n-2)
#print(sum(5))
print(fib(6))