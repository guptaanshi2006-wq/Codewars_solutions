def same_case(a, b): 
    # your code here
    if a.isalpha() and b.isalpha():
        if( a.islower()== True and b.islower()==True) or( a.isupper()== True and b.isupper()==True):
            return 1
        else:
            return 0
    else:
        return -1