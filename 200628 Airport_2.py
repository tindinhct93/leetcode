def findItinerary(tickets):
    List = ["JFK"]
    n = len(tickets)
    def build(List):
        if len(List) == n+1:
            return True
        next = List[-1]
        Child_ele = [ele[1] for ele in tickets if ele[0] == next]
        Child_ele.sort()
        if len(Child_ele) == 0:
            return False
        for element in Child_ele:
            index = tickets.index([next,element])
            List.append(element)
            t = tickets.pop(index)
            if build(List) != True:
                List.pop()
                tickets.append(t)
                continue
            return True
    build(List)
    return List


#a= [["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]
#print(findItinerary(a))
b= [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
print(findItinerary(b))