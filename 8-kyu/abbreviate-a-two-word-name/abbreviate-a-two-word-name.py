def abbrev_name(name):
    name=name.upper()
    add=""
    for i in range(len(name)):
        if name[i]==" ":
            add=name[i+1]
    result=name[0]+"."+ add
    return result