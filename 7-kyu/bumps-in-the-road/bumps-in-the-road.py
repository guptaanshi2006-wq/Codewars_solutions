def bumps(road):
    sum=0
    # your code here
    for i in road:
        if i=="n":
            sum=sum+1
    if sum<=15:
        return "Woohoo!"
    else:
        return "Car Dead"