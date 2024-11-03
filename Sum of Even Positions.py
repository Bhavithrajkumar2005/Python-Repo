def sum_of_even_indexed_elements(arr):
    return sum(arr[i] for i in range(0, len(arr), 2))


N = int(input())
array_elements = list(map(int, input().split()))


result = sum_of_even_indexed_elements(array_elements)
print( result)
