def frange(x, y, jump):
    """function for incrementing small floating point values"""
    while x < y:
        yield x
        x += jump
    return x
