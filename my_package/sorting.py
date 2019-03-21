def bubble_sort(item, asc=True):

    """
    The bubble sort makes multiple passes through a list. It compares
    adjacent items and exchanges those that are out of order. Each pass
    through the list places the next largest value in its proper place.
    In essence, each item “bubbles” up to the location where it belongs.

    """
    lst = list(item)
    for passesLeft in range(len(item)-1, 0, -1):
        for i in range(passesLeft):
            if asc:
                if item[i] > item[i + 1]:
                    item[i], item[i + 1] = item[i + 1], item[i]
            else:
                if item[i] < item[i + 1]:
                    item[i], item[i + 1] = item[i + 1], item[i]
    print(item)

def merge_sort(item):
    """
    The merge sort code pops at the end (efficient enough)
    and sorts inplace despite returning as well.

    """
    if len(item) > 1:
        left, right = map(lambda l: list(reversed(merge_sort(l))), (item[::2], item[1::2]))
        item.clear()
        while left and right:
            item.append(left.pop() if left[-1] < right[-1] else right.pop())
        item.extend(left[::-1])
        item.extend(right[::-1])

    return item

def quick_sort(item):

    '''Return array of items, sorted in ascending order'''

    if len(item) < 2:
        return item
    else:
        quick_sort_lst= item[0]

        less_than = [i for i in item[1:] if i <= quick_sort_lst]

        greater_than = [i for i in item[1:] if i > quick_sort_lst]

        return quick_sort(less_than) + [quick_sort_lst] + quick_sort(greater_than)
