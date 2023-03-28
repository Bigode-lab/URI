while True:
    try:
        n =int(input())
        for i in range(n):
            for j in range(n):
                if(j==(n-1)/2 and i==(n-1)/2):
                    print(4, end='')
                elif((i>=n/3 and j>=n/3) and (i<n-n/3 and j<n-n/3)):
                    print(1, end='')
                elif(i==j):
                    print(2, end='')
                elif(j==n-1-i):
                    print(3, end='')
                else:
                    print(0, end='')
                if(j==n-1):
                    print('')
    except EOFError:
        break