or i in range (0,len(string),k):
        t = string[i:i+k]
        seen = set()
        u = ""
        for ch in t:
            if ch not in seen:
                u += ch
                seen.add(ch)
                print(u)