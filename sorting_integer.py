#!python
from sorting import insertion


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    min_num = min(numbers)
    max_num = max(numbers) + 1

    # TODO: Create list of counts with a slot for each number in input range
    # create list with a length of the value of max_num
    count_list = [0] * max_num

    # TODO: Loop over given numbers and increment each number's count
    # make the counted list by incrementing each instance of a number count
    for i in numbers:
        count_list[i] += 1

    # TODO: Loop over counts and append that many numbers into output list
    comp = 0
    for i in range(0, max_num):
        # make a temporary copy of the count_list index value
        temp = count_list[i]
        # set current loop instance index value to the comp value
        count_list[i] = comp
        # set comp value to temp value
        comp += temp

    # create result list with len of original list with no value
    result = [0] * len(numbers)
    for i in numbers:
        # for each number in list, set the corrisponding
        # result list index to the value of the instance
        result[count_list[i]] = i
        # move to the next index in the count_list for next instance comparison
        count_list[i] += 1
    print(result)
    return result
    # FIXME: Improve this to mutate input instead of creating new output list


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    min_num = min(numbers)
    max_num = max(numbers)
    size = max_num/len(numbers)

    # TODO: Create list of buckets to store numbers in subranges of input range
    bucket_list = []
    for i in range(len(numbers)):
        # make an empty index to represent each bucket
        bucket_list.append([])

    # TODO: Loop over given numbers and place each item in appropriate bucket
    for i in range(len(numbers)):
        j = int(numbers[i]/size)

        #if not last bucket
        if j != len(numbers):
            # append index value of the instance of numbers to the propper bucket
            bucket_list[j].append(numbers[i])
        else:
            # append index value to the last bucket
            bucket_list[len(numbers) - 1].append(numbers[i])

    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    for i in range(len(numbers)):
        # calling insertion sort
        insertion(bucket_list[i])

    # TODO: Loop over buckets and append each bucket's numbers into output list
    result = []
    for i in range(len(numbers)):
        # "append each bucket's numbers into output list"
        result = result + bucket_list[i]

    # print('RESULT: ', result)
    return result


    # FIXME: Improve this to mutate input instead of creating new output list

numbers = [5,4,6,3,7,2,8,1,9,5,0]
print("COUNTING SORT: ", counting_sort(numbers))
print("BUCKET SORT: ", bucket_sort(numbers))
