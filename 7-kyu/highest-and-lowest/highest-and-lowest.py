def high_and_low(number):
    num=[]
    for i in number.split():
        n=int(i)
        num.append(n)
    largest=max(num)
    smallest=min(num)
    return f"{largest} {smallest}"
        
        