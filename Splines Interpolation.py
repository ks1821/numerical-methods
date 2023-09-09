import numpy as np
def Splines(xn,yn,x,va,vb):

# First thing we need to do is to form the matrix
    n = len(xn)-1
    A = np.zeros([n+1,n+1])
    d = np.zeros([n+1])
    v = np.zeros([n+1])
    A[0][0] = 1
    A[n][n] = 1
    d[0] = va
    d[n] = vb



    for j in range(1,n):

        A[j][j-1] = 1/D(xn,j)
        A[j][j] = 2*(1/D(xn,j) + 1/D(xn,j+1))
        A[j][j+1] = 1/(D(xn,j+1))
        d[j] = 3* ( (D(yn,j))/((D(xn,j))**2) + (D(yn,j+1))/((D(xn,j+1))**2) )
    InvA = np.linalg.inv(A) # too lazy to remember inverse.. look over before test though
    v = np.matmul(InvA,d)


# Now that we got da v values, we ought to get the y points!!!
    val = 0
    y = []
    for j in range(0,n):
        a = yn[j]
        b = v[j]
        c = 3*D(yn,j+1)/(D(xn,j+1)**2) - (v[j+1] + 2*v[j])/D(xn,j+1)
        d = -2*D(yn,j+1)/((D(xn,j+1))**3) + (v[j+1]+v[j])/((D(xn,j+1))**2)


        while x[val]<xn[j+1]:
            dx = x[val] - xn[j]
            y = y + [a + b*dx + c*dx**2 + d*dx**3]
            val = val + 1
        if x[val]==xn[n]:
            y = y + [a + b * dx + c * dx ** 2 + d * dx ** 3]

    return y
