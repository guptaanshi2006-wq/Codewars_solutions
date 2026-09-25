def zero_fuel(distance_to_pump, mpg, fuel_left):
    #Happy Coding! ;)
    av=mpg*fuel_left
    if av>=distance_to_pump:
        return True
    else:
        return False