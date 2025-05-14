




def polynomial(A, t):
    y = 0
    for i in range(len(A)):
        y += A[i] * t**i
    return y
    
    