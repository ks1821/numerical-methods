def trapzeqd(x,y):
    I = 0
    sum = 0
    N = len(x)-1
    h = x[1]-x[0]

    for i in range(0,N):
        element = h*(y[i] + y[i+1])*0.5
        sum = sum + element

    I = sum