array = []
N = int(input())
for _ in range (N):
    cmd = input().split()
    if cmd [0] == "insert":
        array.insert(int(cmd[1]),int(cmd[2]))
    elif cmd [0] == "append":
        array.append(int(cmd[1]))
    elif cmd [0] == "remove":
        array.remove(int(cmd[1]))
    elif cmd[0] == "pop":
        array.pop()
    elif cmd[0] == "sort":
        array.sort()
    elif cmd[0] == "reverse":
        array.reverse()
    elif cmd[0] == "print":
        print(array)