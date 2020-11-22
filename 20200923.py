def majorityElement(nums):
    lengh = len(nums)
    dic = {}
    for ele in nums:
        try:
            dic[ele] += 1
        except:
            dic[ele] =1
    t= [*dic]
    def checking(t):
        return dic[t]
    t.sort(reverse= True,key=checking)
    if dic[t[1]]>int(lengh/3):
        return t[:2]
    return [t[0]]

print(majorityElement([1,1,1,3,3,2,2,2]))