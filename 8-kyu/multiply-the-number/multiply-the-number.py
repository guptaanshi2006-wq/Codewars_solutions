def multiply(n):
    i=0
    m=abs(n)
    while m>0:
        m=m//10
        i=i+1
    
    return n*(5**i)