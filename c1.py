def diamond(n):
    # Top half
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
    # Bottom half
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))


# Example usage
rows = int(input("Enter number of rows for half diamond: "))
diamond(rows)
