def is_neon_number(N):
   
    square = N ** 2
    
    
    digit_sum = sum(int(digit) for digit in str(square))
    
    
    if digit_sum == N:
        return "Neon Number"
    else:
        return "Not Neon Number"


N = int(input())


result = is_neon_number(N)
print(result)
