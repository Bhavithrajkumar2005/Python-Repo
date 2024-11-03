def is_prime(num):
    
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_palindrome(num):
    
    return str(num) == str(num)[::-1]

def next_prime_palindrome(N):
   
    candidate = N + 1
    while True:
        if is_prime(candidate) and is_palindrome(candidate):
            return candidate
        candidate += 1


N = int(input())


if 10 <= N <= 10000:
    
    result = next_prime_palindrome(N)
    print(result)
else:
    print()
