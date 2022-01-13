def generate(N):
    # code here
    res = []
    for i in range(1, N+1):
        res.append(str(format(i, 'b')))
    return res
