from peewee import *
from datetime import date

db = SqliteDatabase("people.db")

class Person(Model):
    name = CharField()
    birthdat = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db


class Pet(Model):
    owner = ForeignKeyField(Person, related_name = "pets")
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db


def create_and_conect():
    db.connect()
    db.create_tables([Person, Pet])


def create_family_members():
    uncle_tommy = Person(name = "Tommy", birthdat = date(2000,11,11), is_relative = True)
    uncle_tommy.save()
    grandma_ana = Person.create(name = "Ana", birthdat = date(1960,10,10), is_relative = False)
    grandma_rosa = Person.create(name = "Rosa", birthdat = date(1960,10,10), is_relative = False)
    tommys_dog =  Pet.create(owner = uncle_tommy, name  = "Fido", animal_type = "Dog")
    anas_cat = Pet.create(owner = grandma_ana, name = "wiskas", animal_type = "Cat")

    tommys_dog.name = "firulais"
    tommys_dog.save()

def get_family_members():
    for person in Person.select():
        print("Nombre: {}, Cumpleaños: {}".format(person.name, person.birthdat))


def get_family_member(serch):
    dude = Person.get(Person.name == serch)
    print("{} cumple años el {}".format(dude.name, dude.birthdat))


def delete_pet(nombre):
    #fido = Pet.get(Pet.name == "Fido")
    #fido.delete_instance()
    querry = Pet.delete().where(Pet.name == nombre)
    deleted_entries = querry.execute()
    print("{} deleted entries".format(deleted_entries))

create_and_conect()
delete_pet("wiskas")
