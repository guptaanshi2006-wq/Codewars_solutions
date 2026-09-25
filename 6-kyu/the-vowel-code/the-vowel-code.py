def encode(st):
    for i in st:
        if i=="a":
            st=st.replace("a","1")
        elif i=="e":
            st=st.replace('e',"2")
        elif i=="i":
            st=st.replace("i","3")
        elif i=="o":
            st=st.replace("o","4")
        elif i=="u":
            st=st.replace("u","5")
    return st
    
def decode(st):
    for i in st:
        if i=="1":
            st=st.replace("1","a")
        elif i=="2":
            st=st.replace('2',"e")
        elif i=="3":
            st=st.replace("3","i")
        elif i=="4":
            st=st.replace("4","o")
        elif i=="5":
            st=st.replace("5","u")
    return st