def merge_the_tools(string, k):
    for i in range (0,len(string),k):
        t = string[i:i+k]
        seen = set()
        u = ""
        for ch in t:
            if ch not in seen:
                u += ch
                seen.add(ch)
        print(u)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)