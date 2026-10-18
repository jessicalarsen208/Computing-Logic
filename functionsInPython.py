def greater_than(x, y):
    if x > y:
        return True
    else:
        return False


# Ask the user to enter two numbers
x = int(input("Enter x: "))
y = int(input("Enter y: "))

# Pass both numbers to the function
result = greater_than(x, y)

print("The statement " + str(x) + " is greater than " + str(y)
      + " is " + str(result).lower())
