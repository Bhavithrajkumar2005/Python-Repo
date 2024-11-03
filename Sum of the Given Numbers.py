def add_two_numbers(A, B):
    return A + B
N = int(input())

for _ in range(N):
    A, B = map(int,input().split())
    result = add_two_numbers(A, B)
    print(result)
