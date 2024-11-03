import math

def is_perfect_square(n):
  
    if n < 0:
        return False 
    root = int(math.sqrt(n))  
    return root * root == n  

n = int(input())


if is_perfect_square(n):
    print(f"True")
else:
    print(f"False")
