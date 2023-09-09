import math as mt
def Derivative(xvals,yvals,k):
    dyvals = []
    for n in range(0,len(yvals)-k):
        sum = 0
        for i in range(0,k+1):
            kchoosei = (mt.factorial(k) / (mt.factorial(k - i) * mt.factorial(i)))
            sum = sum + ((-1)**i) * kchoosei * yvals[n + k - i]
        dyvals = dyvals + [sum/(xvals[n+1]-xvals[n])**k]
    return dyvals