
def CompoundSimpsonsthird(yvals,h):
    M = int((len(yvals)-1)/2)
    odds = 0
    evens = 0
    for i in range(1,2*M-1,2):
        odds = odds + yvals[i]
    for i in range(2,2*M-2,2):
        evens = evens + yvals[i]
    integral = h/3 * (yvals[0] + yvals[2*M] + 4*odds + 2 * evens)
    return integral

def Simpsonsthird(yvals,h):
    M = int((len(yvals) - 1) / 2)
    integral = 0
    for i in range(0,2*M-2,2):
        integral += h/3 *(yvals[i] + 4* yvals[i+1] + yvals[i+2] )
    return integral