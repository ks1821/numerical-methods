def trapz(x,y):
    I = 0
    sum = 0
    N = len(x)-1


    for i in range(0,N):
        h = x[i+1] - x[i]   # Quite sure this should be the only big change between this task and task A?!
        element = h*(y[i] + y[i+1])*0.5
        sum = sum + element

    I = sum


    return I
