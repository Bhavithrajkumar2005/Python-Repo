def is_pronic_number(X):
   
    n = 0
    while n * (n + 1) <= X:
        if n * (n + 1) == X:
            return True
        n += 1
    return False


X = int(input())


if is_pronic_number(X):
    print(f"YES")
else:
    print(f"NO")
