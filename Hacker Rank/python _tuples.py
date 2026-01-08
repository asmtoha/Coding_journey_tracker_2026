n = int(input())
elements = tuple(map(int, input().strip().split()))
print(hash(elements))