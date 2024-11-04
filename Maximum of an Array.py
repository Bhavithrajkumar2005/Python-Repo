def find_maximum(arr):
    max_value = arr[0]  
    for num in arr:
        if num > max_value:
            max_value = num
    return max_value


N = int(input())
array_elements = list(map(int, input().split()))


max_element = find_maximum(array_elements)
print(max_element)
