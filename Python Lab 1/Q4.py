print("Q4. Write a code that describes local and global variable with the same name")

# Global variable
variableName = "I am the global variable"

def functionLocalVariable():
    # Local variable with the same name
    variableName = "I am the local variable"
    print(variableName)  # This will print the local variable

functionLocalVariable()
print(variableName)  # This will print the global variable
