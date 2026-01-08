def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line
    # return "-".join(line.split())

line = input()
result = split_and_join(line)
print(result)
