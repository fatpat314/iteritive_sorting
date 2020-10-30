#!python
def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if so
    # loop over indexes of list
    for i in range(len(items)-1):
        # if the value of the current index
        # is greater than the value of the next index
        if items[i] > items[i + 1]:
            # its not sorted, return False
            print(False)
            return False
    # If not stopped, then everything is sorted, return True
    print(True)
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order

    # set the length of the list
    n = len(items)
    # loop over the indexes in the list (-1)
    for i in range(n-1):
        # loop over list from index 0 until len of list - 1
        for j in range(0, n-i-1):
            # if current index is greater than the next index
            if items[j] > items[j+1]:
                # swap
                items[j], items[j+1] = items[j+1], items[j]

    # Check if list is sorted
    if is_sorted(items) == True:
        print(items)


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item

    # loop over indexes in range length of list
    for i in range(len(items)):
        # set the minimum index
        min_index = i
        # loop over indexes following min_index
        for j in range(i+1, len(items)):
            # if the value of the min_index is greater than
            # the value of the current index
            if items[min_index] > items[j]:
                # current index becomes min_index
                min_index = j
        # swap
        items[i], items[min_index] = items[min_index], items[i]

    # Check if list is sorted
    if is_sorted(items) == True:
        print(items)



def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items

    # loop over indexes of list
    for i in range(1, len(items)):
        # set reminder for index value
        key = items[i]

        # set j as the current index - 1
        j = i-1
        # loop while j > 0 and the reminder index calue is less then j's index value
        while j >= 0 and key < items[j]:
            # the index after j is now j
            items[j+1] = items[j]
            # fill the space
            j -= 1
        # set the new j as the reminder comparision key
        items[j+1] = key

    # Check if list is sorted
    if is_sorted(items) == True:
        print(items)

items = [4,8,2,6,3,1,4]
items2 = [1,2,3,4,5,6,7]
print("vvv is_sorted vvv")
is_sorted(items)
print("------------------")
print("vvv bubble_sort vvv")
bubble_sort(items)
print("-------------------")
print("vvv selection_sort vvv")
selection_sort(items)
print("-------------------")
print("vvv insertion_sort vvv")
insertion_sort(items)
