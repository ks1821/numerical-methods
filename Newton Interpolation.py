def NewtDivDifference(xn,yn):
    ndd=0


    if len(xn)==2:
        ndd = (yn[1]-yn[0])/(xn[1]-xn[0])
    else:
        ndd =   NewtDivDifference(xn[1:len(xn)],yn[1:len(yn)]) - NewtDivDifference(xn[0:len(xn)-1],yn[0:len(yn)-1])
        ndd = ndd/(xn[len(xn)-1]-xn[0])


    return ndd


def NewtonInterp(xn,yn,x):
    y = []


    for expansions in range(0,len(x)):
        sum = yn[0]
        for k in range(1,len(xn)):
            product = 1
            for piop in range(0,k):
                product = (x[expansions]-xn[piop])*product
            sum = sum + product*NewtDivDifference(xn[0:k+1],yn[0:k+1])
        y = y + [sum]
    return y