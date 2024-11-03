def is_spy_number(N):
    
    digit_sum = 0
    digit_product = 1
    
   
    for digit in str(N):
        digit = int(digit) 
        digit_sum += digit
        digit_product *= digit
    
   
    if digit_sum == digit_product:
        return "Spy Number"
    else:
        return "Not Spy Number"

N = int(input())


result = is_spy_number(N)
print(result)
