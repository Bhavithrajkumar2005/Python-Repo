def is_disarium_number(n):
    digits = [int(d) for d in str(n)]
    return sum(digit ** (index + 1) for index, digit in enumerate(digits)) == n

N = int(input())

if is_disarium_number(N):
    print("True")
else:
    print("False")
