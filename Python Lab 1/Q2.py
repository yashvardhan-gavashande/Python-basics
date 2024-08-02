print("Q2. Describe Local Variable and Global Variable")
# Global variable

globalVariable = "I am a global variable"
#global variable can be used in any function within the programe

def localVariableFunction():
    #Local variable
    localVariable = "I am a local variable"
    #local variable can be used only within the function
    print(localVariable + " and can be used only within the function")
    print(globalVariable + " and can be used in any function within the programe")

localVariableFunction()
