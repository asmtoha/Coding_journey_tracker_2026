def swap_case(s):
    cng_string = ""
    for ch in s:
        if ch.islower():
            cng_string += ch.upper()
        else:
            cng_string += ch.lower()
    return cng_string
string_to_cng = swap_case(input().strip())
print(string_to_cng)