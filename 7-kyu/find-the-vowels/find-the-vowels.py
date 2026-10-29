def vowel_indices(word):
    # your code here
    words=word.lower()
    arr=[]
    for i in range(len(words)):
        if words[i]=="a"  or words[i]=="e"  or words[i]=="i"  or words[i]=="o"  or words[i]=="u" or words[i]=="y":
            arr.append(i+1)
    return arr
            