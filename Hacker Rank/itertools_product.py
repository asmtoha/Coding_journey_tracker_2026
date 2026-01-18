A = list(map(int,input().split()))
B = list(map(int,input().split()))

products = ((x,y) for x in A for y in B)

print(*products)

# from itertools import product

# print(*product(map(int, input().split()), map(int, input().split())))

