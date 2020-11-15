#!/usr/bin/python3

""" Console Module """

import cmd
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sys import exit


class HBNBCommand(cmd.Cmd):
    """ Class that contains all the methods required to have an interactive
        shell for the specific purpose of the HBNB project.

        Attributes:
            prompt (string): The prompt message shown when requesting an input.
    """

    prompt = "(hbnb) "

    def do_all(self, arg):
        """ Prints all string representation of all instances based or
            not on the class name.

            Ex: (hbnb) all BaseModel or (hbnb) all.
        """

        args = arg.split(' ')

        if args[0] in {"Amenity", "BaseModel", "City", "Place", "Review",
                       "State", "User", ''}:
            list_objs = []
            for value in storage.all().values():
                if args[0] == "Amenity" and type(value) == Amenity:
                    list_objs.append(str(value))
                elif args[0] == "BaseModel" and type(value) == BaseModel:
                    list_objs.append(str(value))
                elif args[0] == "City" and type(value) == City:
                    list_objs.append(str(value))
                elif args[0] == "Place" and type(value) == Place:
                    list_objs.append(str(value))
                elif args[0] == "Review" and type(value) == Review:
                    list_objs.append(str(value))
                elif args[0] == "State" and type(value) == State:
                    list_objs.append(str(value))
                elif args[0] == "User" and type(value) == User:
                    list_objs.append(str(value))
                elif args[0] == '':
                    list_objs.append(str(value))
            print(list_objs)
        else:
            print("** class doesn't exist **")

    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves it (to the JSON file)
            and prints the id.

            Ex: (hbnb) create BaseModel
        """

        args = arg.split(' ')

        if args[0] == '':
            print("** class name missing **")
        elif args[0] in {"Amenity", "BaseModel", "City", "Place", "Review",
                         "State", "User"}:
            if args[0] == "Amenity":
                new_obj = Amenity()
            elif args[0] == "BaseModel":
                new_obj = BaseModel()
            elif args[0] == "City":
                new_obj = City()
            elif args[0] == "Place":
                new_obj = Place()
            elif args[0] == "Review":
                new_obj = Review()
            elif args[0] == "State":
                new_obj = State()
            elif args[0] == "User":
                new_obj = User()
            new_obj.save()
            print(new_obj.id)
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and
            id (saves the change into the JSON file).

            Ex: (hbnb) destroy BaseModel 1234-1234-1234.
        """

        args = arg.split(' ')

        if args[0] == '':
            print("** class name missing **")
        elif args[0] in {"Amenity", "BaseModel", "City", "Place", "Review",
                         "State", "User"}:
            if len(args) >= 2:
                key_id = args[0] + "." + args[1]
                if key_id in storage.all():
                    del storage.all()[key_id]
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_EOF(self, arg):
        """ Quit command to exit the program.

            Ex: (hbnb) EOF.
        """

        exit()

    def do_quit(self, arg):
        """ Quit command to exit the program.

            Ex: (hbnb) quit.
        """

        exit()

    def do_show(self, arg):
        """ Prints the string representation of an instance based on
            the class name and id.

            Ex: (hbnb) show BaseModel 1234-1234-1234.
        """

        args = arg.split(' ')

        if args[0] == '':
            print("** class name missing **")
        elif args[0] in {"Amenity", "BaseModel", "City", "Place", "Review",
                         "State", "User"}:
            if len(args) >= 2:
                for value in storage.all().values():
                    if (value.__class__.__name__ == args[0] and
                            value.id == args[1]):
                        print(value)
                        break
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """ Updates an instance based on the class name and id by adding or
            updating attribute (saves the change into the JSON file).

            Ex: (hbnb) update BaseModel 1234-1234-1234 email "hbnb@hbtn.com".
        """

        args = arg.split(' ')

        if args[0] == '':
            print("** class name missing **")
        elif args[0] in {"Amenity", "BaseModel", "City", "Place", "Review",
                         "State", "User"}:
            if len(args) >= 4:
                key_id = args[0] + "." + args[1]
                if key_id in storage.all():
                    args[3] = args[3].lstrip('"')
                    args[3] = args[3].rstrip('"')
                    setattr(storage.all()[key_id], args[2], args[3])
                    storage.save()
                else:
                    print("** no instance found **")
            elif len(args) == 1:
                print("** instance id missing **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
        else:
            print("** class doesn't exist **")

# Auxiliar functiona

    def emptyline(self):
        """ Does nothing when an empty line is passed as argument to the
            prompt.
        """

        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
