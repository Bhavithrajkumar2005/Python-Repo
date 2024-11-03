def largest_digit(N):
   
    return max(int(digit) for digit in str(N))

N = input()

# Output Format
result = largest_digit(N)
print(f" {result}")
