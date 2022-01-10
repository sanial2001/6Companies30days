def rotate(matrix): 
    #code here
    n = len(matrix)
    
    for g in range(n):
        i = 0
        for j in range(g, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            i = i+1
    
    for i in range(n//2):
        for j in range(n):
            matrix[i][j], matrix[n-i-1][j] = matrix[n-i-1][j], matrix[i][j]
