
def binar_reaserch(list, arge):
    low = 0
    high = len(list) - 1

    while (high >= low):
        mid = (high + low) // 2
        move = list[mid]
        if move == arge:
            return mid
        if move > arge:
            high = mid - 1
        else:
            low = mid + 1

    return None

list = [1, 3 ,5, 7, 9, 15, 23 , 34]

print(binar_reaserch(list, 15))
print(binar_reaserch(list, -3))