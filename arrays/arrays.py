# Find the largest element of an array.
def find_largest(arr):
    if len(arr) == 0:
        return None
    max_elem = arr[0]
    if len(arr) == 1:
        return max_elem
    for elem in arr[1:]:
        max_elem = max(max_elem, elem)
    return max_elem

# Test the function.
test_arr = [1,2,3]
test_max = find_largest(test_arr)
print(test_max)
