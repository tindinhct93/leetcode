import pdb

def findItinerary(tickets):
    def final_des(des, list):
        child_list = [ele[0] for ele in list if ele[1] == des]
        max_child = max(child_list)
        a = list.index([max_child,des])
        return list[a]

    def next_des(des, list):
        child_list = [ele[1] for ele in list if (ele[0] == des and dict[ele[1]] !=1)]
        min_child = min(child_list)
        a = list.index([des,min_child])
        return list[a]

    result = ["JFK"]
    dict = {}
    for ele in tickets:
        try:
            dict[ele[0]] += 1
        except:
            dict[ele[0]] = 1
        try:
            dict[ele[1]] += 1
        except:
            dict[ele[1]] = 1
    #dict['JFK'] -= 1
    for ele in dict:
        if dict[ele] % 2 != 0 and ele !="JFK":
            final = ele
    finaldes = final_des(final, tickets)
    #tickets.remove(finaldes)
    while(len(tickets)>1):
        des = result[-1]
        #pdb.set_trace()
        new = next_des(des,tickets)
        dict[new[0]] -=1
        dict[new[1]] -= 1
        result.append(new[1])
        tickets.remove(new)
    result.append(finaldes[1])
    return result
a= [["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]
print(findItinerary(a))