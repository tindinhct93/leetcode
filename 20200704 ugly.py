def nthUglyNumber(n):
    def update_list(pop_list, num, number):
        for i in range(0, len(pop_list)):
            if pop_list[i] > int(number / num):
                break
            else:
                pop_list.pop(0)

    list = [1, 2, 3, 4, 5, 6, 8, 9, 10]
    list_2 = [6, 8, 9, 10]
    list_3 = [4, 5, 6, 8, 9, 10]
    list_5 = [3, 4, 5, 6, 8, 9, 10]

    def ugly():
        list_t = [list_2[0] * 2, list_3[0] * 3, list_5[0] * 5]
        number = min(list_t)
        list.append(number)
        list_2.append(number)
        list_3.append(number)
        list_5.append(number)
        update_list(list_2, 2, number)
        update_list(list_3, 3, number)
        update_list(list_5, 5, number)

    while len(list) < n:
        ugly()
    return list[n - 1]

print(nthUglyNumber(250))