#!/usr/bin/python3
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter."""

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid."""
        arg_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            arg_list = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg_list[1])
            if match is not None:
                command = [arg_list[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in arg_dict.keys():
                    call = "{} {}".format(arg_list[0], command[1])
                    return arg_dict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    # Function to create a new instance and print its ID
    def do_create(self, arg):
        """Create a new instance of a class and print its ID."""
        arg_list = parse(arg)
        if not arg_list:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj = eval(arg_list[0])()
            obj.save()
            print(obj.id)

    # Function to show the string representation of an instance
    def do_show(self, arg):
        """Display the string representation of an instance."""
        arg_list = parse(arg)
        if not arg_list:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(arg_list[0], arg_list[1])
            obj_dict = storage.all()
            if obj_key in obj_dict:
                print(obj_dict[obj_key])
            else:
                print("** no instance found **")

    # Function to destroy an instance by ID
    def do_destroy(self, arg):
        """Delete an instance by ID."""
        arg_list = parse(arg)
        if not arg_list:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(arg_list[0], arg_list[1])
            obj_dict = storage.all()
            if obj_key in obj_dict:
                del obj_dict[obj_key]
                storage.save()
            else:
                print("** no instance found **")

    # Function to display all instances of a class
    def do_all(self, arg):
        """Display string representations of instances."""
        arg_list = parse(arg)
        obj_dict = storage.all()
        if not arg_list:
            obj_list = [str(obj) for obj in obj_dict.values()]
        elif arg_list[0] in HBNBCommand.__classes:
            obj_list = [str(obj) for obj in obj_dict.values()
                        if obj.__class__.__name__ == arg_list[0]]
        else:
            print("** class doesn't exist **")
            return
        print(obj_list)

    # Function to count instances of a class
    def do_count(self, arg):
        """Retrieve the number of instances of a class."""
        arg_list = parse(arg)
        obj_dict = storage.all()
        count = len([obj for obj in obj_dict.values()
                     if obj.__class__.__name__ == arg_list[0]])
        print(count)

    # Function to update an instance by ID with attributes
    def do_update(self, arg):
        """Update an instance with new attributes or values."""
        arg_list = parse(arg)
        obj_dict = storage.all()
        if not arg_list:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict:
            print("** no instance found **")
        elif len(arg_list) < 3:
            print("** attribute name missing **")
        elif len(arg_list) < 4:
            print("** value missing **")
        else:
            obj = obj_dict["{}.{}".format(arg_list[0], arg_list[1])]
            attr_name = arg_list[2]
            attr_val = arg_list[3].strip('"')
            setattr(obj, attr_name, attr_val)
            obj.save()

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


if __name__ == "__main__":
    HBNBCommand().cmdloop()
