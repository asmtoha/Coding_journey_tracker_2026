from itertools import permutations
S, k = input().split()
for p in permutations(sorted(S),int(k)):
    print("".join(p))