
def Lagrangian(j,xp,xn):
    Lj = 1
    for k in range(0,len(xn)):
        if k!=j:
            Lj = Lj * (xp-xn[k])/(xn[j]-xn[k])
    return Lj

def LagrangianInterp(xn,yn,x):
    y = []
    for points in range(0,len(x)):
        pn = 0
        for j in range(0,len(xn)):
            pn = pn + yn[j]*Lagrangian(j,x[points],xn)
        y = y + [pn]
    return y
