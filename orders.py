# Dealing with files and error/exception handling

# There is a built in method in python called open("")
# file = open("orders.text") # Looks for the file called orders.text
# keyword try
try:
    file = open("orders.text")
    print("file is found")
except FileNotFoundError as errmsg:
    print(f"The above block of code was not executed {errmsg}")
    #raise
finally:
    print("Your task is to read the data and display it as a list")

# second iteration:
# Your task is to read the data and display it as a list"

# 3rd Iteration
# Create a function to the same job DRY