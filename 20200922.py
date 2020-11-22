def carPooling(trips, capacity):
    len = max([e[2] for e in trips])
    result = [0 for i in range(len + 1)]
    for ele in trips:
        start = ele[1]
        end = ele[2]
        passenger = ele[0]
        for i in range(start, end):
            result[i] += passenger
    for ele in result:
        if ele > capacity:
            return False
    return True

a=[[3,2,7],[3,7,9],[8,3,9]]
b=11
print(carPooling(a,b))