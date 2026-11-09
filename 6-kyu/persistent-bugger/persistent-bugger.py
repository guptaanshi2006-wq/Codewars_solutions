def persistence(n):
    # your code
    
    c=0
    while n>9:
        num=n
        p=1
        while num>0:
            p=p*(num%10)
            num=num//10
        n=p
        c=c+1        
    return c