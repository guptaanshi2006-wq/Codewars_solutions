def adjacent_element_product(array):
    res=[]
    for i in range(len(array)-1):
        res.append(array[i]*array[i+1])
    result=sorted(res)
    return result[-1]