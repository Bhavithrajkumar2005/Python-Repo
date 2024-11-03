def is_happy_number(n):
    seen = set()
    
    while n != 1 and n != 7:
        if n in seen:
            return False
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
        
    return True

N = int(input())

if is_happy_number(N):
    print(" True")
else:
    print("False")
