
def mincostTickets(days, costs):
    NumberOfDay = days[-1]
    tickets = [0 for i in range (NumberOfDay)]
    for ele in days:
        tickets[ele-1]=1
    arr=[0]
    for i in range(NumberOfDay):
        if tickets[i]==0:
            arr.append(arr[i])
        else:
            a0 = max(0,i)
            a1 = max(0,i-6)
            a2 = max(0,i-29)
            arr.append(min(arr[a0]+costs[0],arr[a1]+costs[1],arr[a2]+costs[2]))
    return arr[-1]

days = [1,4,6,7,8,20]
costs = [2,7,15]
print(mincostTickets(days,costs))