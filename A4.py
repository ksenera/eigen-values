"""
PROJECT   : A4.py
PROGRAMMER: Kushika Senera
COURSE    : SFWRTECH 4MA3 - Numerical Linear Algebra and Numerical Optimization
INSTRUCTOR: Gagan Sidhu
DATE: Tuesday, March 10th 
"""

# lower triangle system Lx = b
def forwardSub(L, b):
    # declare and initialize output vector x
    n = len(b)
    x = [0.0] * n
    # for j = 1 to n {loop over cols.} 
    # got length of b vector and put it in n to start loop
    for j in range(n):
        # xj = bj/Ljj {compute soln. component}
        x[j] = b[j] / L[j][j]

        # for i = j + 1 to n 
        # j starts at index 0 so j + 1 = 1 & n = 4 so from index 1 up to index 3 
        # range start to stop index n-1 => 4-1 = 3 
        for i in range(j+1,n):
            # bi = bi - Lijxj {update RHS}
            b[i] = b[i] - L[i][j] * x[j]
    return x

# upper triangle system Ux = b 
def backSub(U, b):
    # declare and initialize output vector x
    n = len(b)
    x = [0.0] * n
    # for j = n to 1 {loop backwards over cols.} 
    for j in reversed(range(n)):
        # xj = bj/Ujj {compute soln. component}
        x[j] = b[j] / U[j][j]
        # for i = 1 to j - 1
        # range starts at 1 and stops at j-1
        # using range(stop) => j => j-1 
        for i in range(j):
            # bi = bi - uijxj {update RHS}
            b[i] = b[i] - U[i][j] * x[j]
    return x


# from hints
def RayleighQuotient(A, x, tolerance):
    pass

def qrIteration(A, tolerance):
    pass