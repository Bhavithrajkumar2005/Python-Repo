def find_minimum(arr):
    min_value = arr[0] 
    for num in arr:
        if num < min_value:
            min_value = num
    return min_value


N = int(input())
array_elements = list(map(int, input().split()))


min_element = find_minimum(array_elements)
print(min_element)
