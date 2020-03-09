class Dog():

    # CLASS OBJECT ATRIBUTES
    species = "mammal" # default

    def __init__(self, breed, name): # defined when iniciated
        self.breed = breed # this always has to go
        self.name = name


my_dog = Dog(breed="lab", name="Sammy")
# my_dog = Dog("lab", "Sammy")  # same

# other_dog = Dog(breed="Huskie")
print(my_dog.breed)
print(my_dog.name)
print(my_dog.species)
# print(other_dog.breed)




class Circle():


    pi = 3.14


    def __init__(self, radius=1): # if not provided default of radius will be 1
        self.radius = radius # this always has to go!!!


    def area(self): # it has to take self becouse its inside of a class
        return self.radius * self.radius * Circle.pi # we have to put self again becouse its a variable thats inside of a class


    def set_radius(self, new_r):
        self.radius = new_r


my_circle = Circle(3)
my_circle.set_radius(999)
print(my_circle.area())




# INHERITANCE
class Animal():


    def __init__(self):
        print("ANIMAL CREATED")


    def who_am_i(self):
        print("ANIMAL")


    def eat(self):
        print("EATING")


class Cat(Animal):


    def __init__(self):
        # Animal.__init__(self) # esto no es necesario
        print("CAT CREATED")


    def miaw(self):
        print("MIAWWW")


    def eat(self):
        print("CAT EATING")





mya = Cat()
mya.who_am_i()
mya.eat()
mya.miaw()





# SPECIAL METHODS

class Book():


    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


    def __str__(self):
        return "Book title: '{}', by {}. Pages {}".format(self.title, self.author, self.pages)


    def __len__(self):
        return self.pages


    def __del__(self): # this method is used when you dekete an object
        print("a book is destroyed")


b = Book("Python", "Daniel", 200)
print(b)
print(len(b))
