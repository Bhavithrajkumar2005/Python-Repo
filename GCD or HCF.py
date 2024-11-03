import math

def find_gcd(N, M):
   
    return math.gcd(N, M)


N, M = map(int, input().split())


gcd_result = find_gcd(N, M)
print(f"  {gcd_result}")
