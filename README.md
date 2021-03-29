# Dealing with files and Exception Handling in Python
## We have `try`, `except`, `raise` and `finally` as our code blocks to handle the error or an exceptions

### To understand the concept easily -
- Each block of code works as an if, elif, else block
```
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

```
- Please ensure to create an orders.text if does not exist 

| Mode	 |Description|
| :----: |:----                                                    |
|'r'	 |This is the default mode. It Opens file for reading.       |
|'w'	 |This Mode Opens file for writing.  If file does not exist, it creates a new file. If file exists it truncates the file.|
|'x'	 |Creates a new file. If file already exists, the operation fails.|
|'a'	 |Open file in append mode. If file does not exist, it creates a new file.|
|'t'	 |This is the default mode. It opens in text mode.|
|'b'	 |This opens in binary mode.
|'+'	 |This will open a file for reading and writing (updating)|


It is worth noting that the `+` operator can be used with 

```python
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

```
- Let's add an item to our orders.text

```python
def write_to_file(file, order_item):
    try:
        with open(file, "w") as file:
            file.write(order_item + '\n')
    except FileNotFoundError:
        print("file cannot be found or directory is incorrect, please check the details provided")
        raise

write_to_file("order.txt", "Ice Cream")
```