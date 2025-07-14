# This program prints the multiplication table for a given number from 1 to 10.

number = int(input("Enter a number to see its multiplication table: "))

for num in range(1, 11):
    print(f"{number} * {num} = {number * num}")
