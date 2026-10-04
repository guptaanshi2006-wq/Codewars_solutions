def generate_shape(n):
    ar = ""
    for i in range(n):
        for j in range(n):
            ar =ar+ "+"
        if i < n - 1:  
            ar += "\n"
            
    return ar