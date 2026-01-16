# how many substrings can be formed? From index i, number of substrings = n - i

def minion_game(string):
    vowels = "AEIOUaeiou"
    n = len(string)
    stuart = 0
    kevin = 0
    for i in range(n):
        if string[i] in vowels:
            kevin += n-i
        else:
            stuart += n-i
    if stuart > kevin:
        print(f"Stuart {stuart}")
    elif kevin > stuart:
        print(f"Kevin {kevin}")
    else:
        print("Draw")
            
if __name__ == '__main__':
    s = input()
    minion_game(s)