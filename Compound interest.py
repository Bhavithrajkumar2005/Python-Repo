def calculate_compound_interest(P, R, T):
    
    A = P * (1 + R / 100) ** T
    return round(A, 2)

P, R, T = map(float, input().split())


total_amount = calculate_compound_interest(P, R, T)


print(f" {total_amount:.2f}")
