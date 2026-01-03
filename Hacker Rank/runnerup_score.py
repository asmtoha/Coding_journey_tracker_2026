n=int(input())
a = map(int,input().split())
unique_scores = sorted(list(set(a)))
print(unique_scores[-2])