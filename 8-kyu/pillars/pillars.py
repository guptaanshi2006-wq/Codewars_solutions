def pillars(num_pill, dist, width):
    n=num_pill
    if n<=1:
        return 0
    d= ((n-1)*dist*100)+((n-2)*width)
    return d