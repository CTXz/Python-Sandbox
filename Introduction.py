# Simple user I/O script that introduces someone

# Get some data about the user
age = input("Enter your age: ")   # Get age from user (age will be returned as str)
name = input("Enter your name: ") # Get name fro user

# Introduce
print("Let me introduce you to " + name + " he's " + age + " years old")

age = int(age) # Convert to int

print("He'd be", age * 2, "years old if he was twice as old as now")
