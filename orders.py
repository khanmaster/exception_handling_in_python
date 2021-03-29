# # Dealing with files and error/exception handling
#
# # There is a built in method in python called open("")
# # file = open("orders.text") # Looks for the file called orders.text
# # keyword try
# try:
#     file = open("orders.text")
#     print("file is found")
# except FileNotFoundError as errmsg:
#     print(f"The above block of code was not executed {errmsg}")
#     #raise
# finally:
#     print("Your task is to read the data and display it as a list")

# second iteration:
# Your task is to read the data and display it as a list"

# 3rd Iteration
# Create a function to the same job DRY
def open_using_with_and_print(file):
    try:
        with open(file, "r") as file:
            for line in file.readlines():
                print(line.rstrip('\n'))
    except FileNotFoundError:
        print("file cannot be found or directory is incorrect, please check the details provided")
        raise
    finally:
        print("\nPlease chose the items from the list  and enjoy your HAPPY MEAL")
open_using_with_and_print("orders.text")

# fourth iteration
# add desert and Ice cream to orders.text

def write_to_file(file, order_item):
    try:
        with open(file, "w") as file:
            file.write(order_item + '\n')
    except FileNotFoundError:
        print("file cannot be found or directory is incorrect, please check the details provided")
        raise

write_to_file("order.txt", "Ice Cream")
open_using_with_and_print("order.txt")