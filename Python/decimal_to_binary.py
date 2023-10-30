"""
change decimal to binary
"""
decimal = int(input("Enter the decimal number"))
remainder = 0
while decimal > 1:
    remainder = decimal % 2
    print(remainder)
    decimal //= 2
    remainder += 1
    digit = len(str(decimal))
    for i in range(digit):
        print(i + 1, end=" ")
