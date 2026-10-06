def filter_string(st):
    num=""
    for i in st:
        if i.isdigit():
            num=num+i
    number=int(num)
    return number