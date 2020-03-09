import datetime
import sys

from peewee import *

from collections import OrderedDict

db = SqliteDatabase("diary.db")


class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


def create_and_conect():
    """Connects to the database and creates the tables"""
    db.connect()
    db.create_tables([Entry], safe=True)


def menu_loop():
    """Show menu"""
    print()
    choise = None
    while choise != "q":
        print("\n")
        print("Press 'q' to quit")
        for key, value in menu.items():
            print("{}) {}".format(key, value.__doc__))

        choise = input("Action: ").lower().strip()

        if choise in menu:
            menu[choise]()


def add_entry():
    """Add Entry to the diary"""
    print("Enter your thoughts.")
    print("Press 'ctr + Z on Windows or ctr + D on Mac' to finish")
    data = sys.stdin.read().strip()

    if data:
        if input("Do you want to save your entry? [y/n]").lower() != "n":
            Entry.create(content=data)
            print("Your entry was saved successfully")


def view_entries(search_query=None, type_of_query=None):
    """View all entries"""
    entries = Entry.select().order_by(Entry.timestamp.desc())

    if search_query and type_of_query == 1:
        entries = entries.where(Entry.content.contains(search_query))
    elif search_query and type_of_query == 2:
        entries = entries.where(Entry.timestamp == search_query)

    number = 0
    try:
        while True:
            entry = entries[number]
            print_entry(entry, number)
            number += 1
    except IndexError:
        print("End of entries list")
        print("d) delete an entry")
        print("e) Edit an entry")
        print("q) return to menu")

        next_action = input("Action[d/e/q]: ").lower().strip()
        if next_action == "q":
            menu_loop()
        elif next_action == "d":
            try:
                entry_number = int(input(
                    "Select the number of the entry you want to delete: "))
            except ValueError:
                print("Thats not a valid Entry")
            else:
                try:
                    print_entry(entries[entry_number], 0)
                except IndexError:
                    print("That element doesent exists\n\n")
                    view_entries()
                else:
                    delete_entry(entries[entry_number])
        elif next_action == "e":
            try:
                entry_number = int(input(
                    "Select the number of the entry you want to update: "))
            except ValueError:
                print("Thats not a valid Entry")
            else:
                try:
                    print_entry(entries[entry_number], 0)
                except IndexError:
                    print("That element doesent exists\n\n")
                    view_entries()
                else:
                    edit_entry(entries[entry_number])


def print_entry(entry, number):
    timestamp = entry.timestamp.strftime("%A %B %d, %Y %I:%M%p")
    number_and_time = "Entry number: {} date: {} ".format(number, timestamp)
    print(number_and_time)
    print("-" * len(number_and_time))
    print("\n")
    print(entry.content)
    print("\n")
    print("-" * len(timestamp))


def search_entries():
    """Search for entries with text"""
    search_query = input("Search query: ").strip()
    view_entries(search_query, 1)


def search_entries_date():
    """Search for entries with a date"""
    search_query = input("Search query: ").strip()
    view_entries(search_query, 2)


def delete_entry(entry):
    """Delete an entry"""
    action = input("Are you sure you want to delete this entry?[y/n] ").lower()

    if action == "y":
        entry.delete_instance()
        print("Entry was deleted successfully")


def edit_entry(entry):
    """Edit a selected entry"""
    print("Enter your thoughts.")
    print("Press 'ctr + Z on Windows or ctr + D on Mac' to finish")
    data = sys.stdin.read().strip()

    if data:
        if input("Do you want to save your entry? [y/n]").lower() != "n":
            entry.content = data
            entry.save()
            print("Your entry was saved successfully")


menu = OrderedDict([
    ("a", add_entry),
    ("v", view_entries),
    ("s", search_entries),
    ("ss", search_entries_date)
])


if __name__ == '__main__':
    create_and_conect()
    menu_loop()
