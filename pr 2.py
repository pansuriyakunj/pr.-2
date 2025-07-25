print("Welcome to the Pattern Generator and Number Analyzer!\n")

print("1. Right-angled Triangle")
print("2. Pyramid")
print("3. Left-angled Triangle")
print("4. Analyze a Range of Numbers")

choice = int(input("Enter your choice: "))

if choice == 1:
    rows = int(input("Enter the number of rows: "))
    if rows > 0:
        print("\nPattern:")
        for i in range(1, rows + 1):
            print("*" * i)
    else:
        print("Invalid input. Number of rows must be positive.")

elif choice == 2:
    rows = int(input("Enter the number of rows: "))
    if rows > 0:
        print("\nPattern:")
        for i in range(1, rows + 1):
            print(" " * (rows - i) + "*" * (2 * i - 1))
    else:
        print("Invalid input. Number of rows must be positive.")

elif choice == 3:
    rows = int(input("Enter the number of rows: "))
    if rows > 0:
        print("\nPattern:")
        for i in range(1, rows + 1):
            print(" " * (rows - i) + "*" * i)
    else:
        print("Invalid input. Number of rows must be positive.")

elif choice == 4:
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    if start <= end:
        total = 0
        for i in range(start, end + 1):
            if i % 2 == 0:
                print("Number", i, "is Even")
            else:
                print("Number", i, "is Odd")
            total += i
        print("Sum of all numbers from", start, "to", end, "is:", total)
    else:
        print("Invalid range. Start should be less than or equal to End.")

else:
    print("Invalid choice.")
    


"""
Welcome to the Pattern Generator and Number Analyzer!

1. Right-angled Triangle
2. Pyramid
3. Left-angled Triangle
4. Analyze a Range of Numbers
Enter your choice: 1
Enter the number of rows: 5

Pattern:
*
**
***
****
*****
"""
