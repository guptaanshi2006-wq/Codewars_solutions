def find_multiples(integer, limit):
    # Your code here!
    arr=[]
    val=integer
    while val<=limit:
        arr.append(val)
        val=val+integer       
    return arr
        
        
        