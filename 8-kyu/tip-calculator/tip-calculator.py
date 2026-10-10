import math
def calculate_tip(amount, rating):
    #your code here
    rating=rating.lower()
    match rating:
        case "terrible":
             return 0
        case "poor":
            return math.ceil(amount*0.05)
        case "good":
            return  math.ceil(amount*0.10)
        case "great":
            return  math.ceil(amount*0.15)
        case "excellent":
            return  math.ceil(amount*0.20)
        case _:
            return "Rating not recognised"
        
            