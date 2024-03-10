
def find_smalest(list):
    smallest = list[0]

    for i in range(1, len(list)):
        if list[i] < smallest:
            smallest = list[i]

    return smallest

def sort_list(list):
    newList = []
    size = len(list)
    for i in range(7):
        smallest = find_smalest(list)
        newList.append(smallest)
        list.remove(smallest)
    return newList


print(find_smalest([12,4,5,3,6,2,10]))
print(sort_list([12,4,5,3,6,2,10]))


