def binary_search(input_array, value):

    first = 0
    last = len(input_array)-1
    found = -1

    while first<=last:
        mid = (first + last)//2
        if input_array[mid] == value:
            return mid
        else:
            if value < input_array[mid]:
                last = mid-1
            else:
                first = mid+1
    return -1


test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
