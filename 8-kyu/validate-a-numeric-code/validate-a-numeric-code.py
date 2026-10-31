def validate_code(code):
    codes=str(code)
    #your code here
    if codes.startswith(("1","2","3")) :
        return True
    return False