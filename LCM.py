import math
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


a, b = map(int, input().split())
result = lcm(a, b)
print(result)