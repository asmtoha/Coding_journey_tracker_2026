import string
def print_rangoli(size):
    alpha = string.ascii_lowercase
    width = 4*size-3
    lines = []
    
    for i in range(size):
        left = alpha[n-1:n-i-1:-1]
        right = alpha[n-i-1:n]
        line = "-".join(left+right)
        lines.append(line.center(width,"-"))
    print("\n".join(lines + lines[-2::-1]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)