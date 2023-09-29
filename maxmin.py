def final_max_min(arr):
    arr.sort()
    max_min = {"max": arr[-1], "min": arr[0]}
    return max_min


input_of_arr = input(
    'Please enter a all elements of the list separated by a space.\n')
arr = input_of_arr.split()
max_min = final_max_min(arr)

print('The minimum number is: ' + max_min["min"])
print('The maximum number is: ' + max_min["max"])
