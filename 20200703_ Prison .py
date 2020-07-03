def prisonAfterNDays(cells, N):
    a = 0
    n = N%14
    s = []
    for i, ele in enumerate(cells):
        a += ele * 2 ** (7 - int(i))
    for i in range(0, n+14):
        a = (~(a << 1 ^ a >> 1)) & 126
        s.append(a)
    str_a = f'{a:08b}'
    result = []
    for i in str_a:
        result.append(int(i))
    return result

print(prisonAfterNDays([1,0,0,1,0,0,0,1],826))
