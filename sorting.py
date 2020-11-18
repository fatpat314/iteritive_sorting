# While list is not sorted
    # for each item in list
        # if this item is > next item:
            # swap
        # else
            # pass
list = [12, 11, 13, 5, 6]

def insertion(list):
    # loop through range of length of list
    for i in range(1, len(list)):
        # set reminder for index value
        key = list[i]

        # set j as the current index - 1
        j = i-1
        # loop while j > 0 and the reminder index calue is less then j's index value
        while j >= 0 and key < list[j]:
            # the index after j is now j
            list[j+1] = list[j]
            # fill the space
            j -= 1
        # set the new j as the reminder comparision key
        list[j+1] = key
    # print(list)
    return(list)

insertion(list)
# for i in range(len(list)):
#     print(list[i])
