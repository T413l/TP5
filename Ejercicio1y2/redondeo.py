from math import ceil,floor
def redondear (x):
    if x >=(int(x)+ 0.5):
        return ceil(x)
    else:
        return floor(x)