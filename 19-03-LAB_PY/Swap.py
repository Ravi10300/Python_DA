
# Q2). Using input function take two number and then swap the number

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

print("You Are Enter First",a)
print("You Are Enter Second",b)

print("-------After Swapping This Number-------")
a,b = b,a            # Swapping Statement
print("Now First Number is",a)
print("Now Secnod Number is",b)
