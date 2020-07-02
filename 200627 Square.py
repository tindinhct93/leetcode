import math
def find(n):
    list = [i*i for i in range(1,int(math.sqrt(n))+1)]
    result = [0 for i in range(0,n+1)]
    for i in range(1,n+1):
        result[i] = min(result[i-w] for w in list if w<=i) +1
    return result[n]

print(find(12))
