# This program prints a square pattern of stars based on user input.

integer = int(input("Enter the size of the pattern: "))
row = 0

while row < integer:
    for _ in range(integer):
        print("*", end="")
    print()  # move to the next line after printing one row
    row += 1
