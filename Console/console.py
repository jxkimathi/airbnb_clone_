#!/usr/bin/python3
"""Contains the entry point of the command interpreter"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """Class containing the command methods"""
    prompt = "(hbnb) "

    classes = ["BaseModel", "User", "Amenity", "City", "Place", "Review", "State"]

    integers = ["number_rooms", "number_bathrooms", "max_guest", "price_by_night"]

    floaters = ["longitude", "latitude"]

    strings = ["name", "email", "password", "first_name", "last_name"]

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id."""
        args = arg.split()
        classes_models = {
            "BaseModel": BaseModel,
            "User": User
        }
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            if args[0] in classes_models:
                new_instance = classes_models[args[0]]()
            storage.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        all_objects = storage.all()

        if key not in all_objects:
            print("** no instance found **")
        else:
            print(all_objects[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                storage.all().pop(key)

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name."""
        args = arg.split()
        my_list = []
        if len(args) >= 1:
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for key, value in storage.all().items():
                class_name = key.split('.')[0]
                if args[0] == class_name:
                    my_list.append(str(value))
        else:
            for key, value in storage.all().items():
                my_list.append(str(value))
        print(my_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(args) == 2:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        elif len(args) >= 4:
            key = args[0] + "." + args[1]
            match = args[3]
            if args[2] in HBNBCommand.strings:
                setattr(storage.all()[key], args[2], str(match))
            elif args[2] in HBNBCommand.integers:
                setattr(storage.all()[key], args[2], int(match))
            elif args[2] in HBNBCommand.floaters:
                setattr(storage.all()[key], args[2], float(match))
            else:
                setattr(storage.all()[key], args[2], match)
            storage.save()

    def emptyline(self, line):
        """Overrides the emptyline"""
        pass

    def do_EOF(self, line):
        """Ctrl+D for exiting the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
