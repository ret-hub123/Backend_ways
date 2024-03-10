"""def sum(list):
    if list == []:
        return 0
    else:
        return list[0] + sum(list[1:])

list = [2, 4 , 6]
print(sum(list))"""

print("")
print("--------------------------------------")
print("")

"""def index_col(list):
    if list == []:
        return 0
    else:
        return 1 + index_col(list[1:])

list = [2, 4 , 6]
print(index_col(list))"""

print("")
print("--------------------------------------")
print("")

def bin_reaserch_recursion(list, item, start, end):
        if end > start:
            mid = (start + end) // 2
            if list[mid] > item:
                end = mid
                return bin_reaserch_recursion(list, item, start, end)
            if list[mid] < item:
                start = mid
                return bin_reaserch_recursion(list, item, start, end)
            if list[mid] == item:
                return mid
        else:
            return 0


list = [ 3 ,5, 7, 10]

print(bin_reaserch_recursion(list, 6, 0, (len(list)-1)) )
print(3//2)



