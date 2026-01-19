from collections import Counter 
n_shoes = int(input())
sizes  = list(map(int,input().split()))
inventory = Counter(sizes)
n_customers = int(input())
total_earning = 0
for _ in range (n_customers):
    size,price = map(int,input().split())
    if inventory[size] > 0:
        total_earning += price
        inventory[size] -= 1
print(total_earning)