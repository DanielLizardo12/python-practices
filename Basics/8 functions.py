def my_func(parameter = "default"):
    """
    this function is the shit
    """
    print("my first function {}".format(parameter))

my_func("daniel")


def hello():
    return "Hello"

result = hello()

print(result)


def add_number(num1, num2):
    if type(num1) == type(num2) == type(10):
        return num1 + num2
    else:
        return "sorry i need integers"


result = add_number("2", "3")
print(result)


# lambda Expression
# Filter
my_list = [1,2,3,4,5,6,7,8]

# def even_bool(num):
#     return num%2 == 0
#
# evens = filter(even_bool,my_list)
# print(list(evens))
# or
evens = filter(lambda num:num%2 == 0,my_list)
print(list(evens))


tweet = "Go Sports #Sports"
result = tweet.split("#")[1]
print(result)


print ("x" in [1,2,3,"x"])
