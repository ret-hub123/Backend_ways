def fast_sort(list):
    if len(list) < 2:
        return list
    else:
        main = list[0]
        small = []
        big = []

        for i in (list[1:]):
            if main > i:
                small.append(i)
            else:
                big.append(i)

        return fast_sort(small) + [main] + fast_sort(big)


print(fast_sort([2, 5 , 3 , 1 ,4]))