x = 25


def my_func():
    x = 50
    return x



my_func()
print(x)



# LOCAL
lambda x: x**2

# Enclosing function locals
name = "this is a global name!"


def greet():
    name = "sammy"

    def hello():
        print("hello " + name)

    hello()

greet()
print(name)



# Built in level
x = 50

def func():
    # print("x is: ", x)
    # x = 1000
    # print("local x changed to: ", x)
    global x
    x = 1000

print("before function call, x is: ", x)
func()
print("after function call, x is: ", x)
