

def triangle1(n):
    for i in range(n):
        print(' '*(n-i-1)+'*'*(2*i+1))

triangle1(10)

print('---------------------------')

def triangle2(n):
    ns = n - 1 # number of spaces

    for i in range(0, n): # handle number of rows
        for j in range(0, ns): # handle number of spaces
            print(end=' ')
        
        ns = ns - 1

        for j in range(0, i+1): # printing stars
            print('*', end=' ') 
        print('\r')

triangle2(10)