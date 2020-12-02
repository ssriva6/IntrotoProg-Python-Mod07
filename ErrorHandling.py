# Structured Error Handling Example------------------------------------------------------#

# An exception occurs when normal flow of the programs instructions are interrupted.
# Exception using numbers:
print("This Excersize is to calculate the Quotient of Two Numbers")
try:
    num1=int(input("Enter first number to calculate quotient:"))

except ValueError:
    print("Enter numbers only")
else:
    try:
        num2=int(input("Please enter a second number:"))
    except ValueError:
        print("Enter numbers only")
    else:
        try:
            num1/num2
        except ZeroDivisionError:
            print("Re-Enter Second Number: can't be zero")
        else:
            print(num1/num2)


