def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def nearest_prime(N):
    if N < 2:
        return 2  
    lower = N
    upper = N
    
    while True:
        if is_prime(lower):
            return lower
        if is_prime(upper):
            return upper
        
        lower -= 1
        upper += 1


T = int(input())
results = []

for _ in range(T):
    N = int(input())
    results.append(nearest_prime(N))


for result in results:
    print(result)
