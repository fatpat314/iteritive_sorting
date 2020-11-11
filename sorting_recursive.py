#!python


def merge(left, right, items):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    # length of each half
    left_size = len(left)
    right_size = len(right)

    # counters for each half
    i = 0
    j = 0

    # main counter
    counter = 0

    # TODO: Repeat until one list is empty
    while i < left_size and j < right_size:

        # TODO: Find minimum item in both lists and append it to new list
        # if our left instance is less than our right instance
        if left[i] < right[j]:
            # put our left instance into our main list index
            items[counter] = left[i]
            # increment left index
            i += 1
        # our right instance is smaller
        else:
            # put the right instance into our main list index
            items[counter] = right[j]
            # increment right index
            j += 1
        # increment main index
        counter += 1

    # TODO: Append remaining items in non-empty list to new list
    while i < left_size:
        items[counter] = left[i]
        i += 1
        counter += 1

    while j < right_size:
        items[counter] = right[j]
        j += 1
        counter += 1


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    if len(items) > 1:

        # # TODO: Split items list into approximately equal halves
        mid = len(items)//2
        left = items[:mid]
        right = items[mid:]
        # print('left: ', left)
        # print('rignt: ', right)

        # # TODO: Sort each half by recursively calling merge sort
        merge_sort(left)
        merge_sort(right)

        # TODO: Merge sorted halves into one list in sorted order
        merge(left, right, items)


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    # Set our instance to the lowest index
    i = (low-1)
    # TODO: Choose a pivot any way and document your method in docstring above
    """ pivot is set to the highest index of items  """
    pivot = items[high]
    # print('pivot: ', pivot)
    # print(items)

    # TODO: Loop through all items in range [low...high]
    for j in range(low, high):
        # TODO: Move items less than pivot into front of range [low...p-1]
        if items[j] <= pivot:
            i = i+1
            # swap
            items[i], items[j] = items[j], items[i]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    items[i+1], items[high] = items[high], items[i+1]

    # TODO: Move pivot item into final position [p] and return index p
    return (i+1)



def quick_sort(items, low, high):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    if low == None or high == None:
        print('Oops')
        return
    # TODO: Check if list or range is so small it's already sorted (base case)
    if len(items) <= 1:
        return items

    if low < high:
        # TODO: Partition items in-place around a pivot and get index of pivot
        pi = partition(items, low, high)

        # TODO: Sort each sublist range by recursively calling quick sort
        quick_sort(items, low, pi-1)
        quick_sort(items, pi+1, high)
        # print(items)


# unsorted
items = [5,2,6,4,7,3,8,9,1]

# empty
# items = []

# single
# items = [5]

# sorted
# items = [1,2,3,4,5,6,7,8,9]

# same
# items = [5,5,5,5,5,5,5,5,5]
print('merge_sort Unsorted: ', items)
merge_sort(items)
print('merge_sort Sorted Result: ', items)

print('---------------------------------')

# unsorted
items = [5,2,6,4,7,3,8,9,1]

# empty
# items = []

# single
# items = [5]

# sorted
# items = [1,2,3,4,5,6,7,8,9]

# same
# items = [5,5,5,5,5,5,5,5,5]
print('quick_sort Unsorted: ', items)
n = len(items)
quick_sort(items, 0, n-1)
print('quick_sort Sorted Result: ', items)
