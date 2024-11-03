def is_fibonacci(num):
  
    if num < 0:
        return False
    
   
    a, b = 0, 1
   
    while a < num:
        a, b = b, a + b
        
   
    return a == num

N = int(input())

# Output Format
if is_fibonacci(N):
    print(f" True" )
else:
    print(f" False " )
