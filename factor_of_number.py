# Python Program to Find the Factors of a Number

def fact(n):
    print(n)
    if n==1:
        return n
    else:
        return n * fact(n-1)
    
print(fact(5))