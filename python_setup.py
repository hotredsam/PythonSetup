# Function to print a greeting to the user
def hello():
    print("Hello, user!")

# Function that accepts three arguments and returns them in a list
def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]

# Function to simulate eating lunch from a list
def eat_lunch(lunch_list):
    if len(lunch_list) == 0:
        print("My lunchbox is empty!")
    else:
        print(f"First I eat {lunch_list[0]}")
        for food in lunch_list[1:]:
            print(f"Next I eat {food}")

# Test the functions
hello()

packed_list = pack("apple", "banana", "orange")
print("Output of pack function:", packed_list)

eat_lunch(["sandwich", "chips", "juice"])
eat_lunch([])
