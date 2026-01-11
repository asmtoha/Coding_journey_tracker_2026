def print_formatted(number):
    width = len(bin(number))-2

    for i in range(1, number + 1):
        decimal = format(i, "d")
        octal = format(i, "o")
        hexa = format(i, "X")
        binary = format(i, "b")
        print(
            f"{decimal.rjust(width)} {octal.rjust(width)} {hexa.rjust(width)} {binary.rjust(width)}"
        )


if __name__ == "__main__":
    n = int(input())
    print_formatted(n)
