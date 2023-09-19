def finalmaxmin(arr):
    arr.sort()
    maxmin = {"max": arr[-1], "min": arr[0]}
    return maxmin


input_of_arr = input(
    'Please enter a all elements of the list separated by a space.\n')
arr = input_of_arr.split()
maxmin = finalmaxmin(arr)

print('The minimum number is: ' + maxmin["min"])
print('The maximum number is: ' + maxmin["max"])
