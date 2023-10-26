#!/usr/bin/python3
"""The definition of the HBnB console."""
import cmd
import json
import datetime
import uuid
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    intro = "Welcome hbnb"
    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def do_create(self, line):
        """Create a new instance of BaseModel."""
        if not line:
            print("** class name missing **")
        elif line not in BaseModel.__subclasses__():
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Print the string representation of instance (class name and id.)"""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in BaseModel.__subclasses__():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = args[0] + "." + args[1]
            obj_dict = storage.all()
            obj = obj_dict.get(obj_key)
            if obj is None:
                print("** no instance found **")
            else:
                print(obj)

    def do_destroy(self, line):
        """Deletes an instance based on class name and id."""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in BaseModel.__subclasses__():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = args[0] + "." + args[1]
            obj_dict = storage.all()
            obj = obj_dict.get(obj_key)
            if obj is None:
                print("** no instance found **")
            else:
                del obj_dict[obj_key]
                storage.save()

    def do_all(self, line):
        """Print all string representations of instances."""
        args = line.split()
        obj_list = []
        obj_dict = storage.all()

        if not args:
            for obj in obj_dict.values():
                obj_list.append(str(obj))
            print(obj_list)
        elif args[0] not in BaseModel.__subclasses__():
            print("** class doesn't exist **")
        else:
            for key, obj in obj_dict.items():
                if key.split('.')[0] == args[0]:
                    obj_list.append(str(obj))
            print(obj_list)

    def do_update(self, line):
        """Updates an instance with a new attribute value."""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in BaseModel.__subclasses__():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = args[0] + "." + args[1]
            obj_dict = storage.all()
            obj = obj_dict.get(obj_key)
            if obj is None:
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                attr_name = args[2]
                attr_value = args[3]
                if hasattr(obj, attr_name):
                    attr_value = eval(attr_value)
                    setattr(obj, attr_name, attr_value)
                    obj.save()
                else:
                    print("** attribute doesn't exist **")

    def do_exit(self, line):
        """Exit the command-line interpreter."""
        return True

    def do_quit(self, line):
        """Exit the command-line interpreter."""
        return self.do_exit(line)

    def help_exit(self):
        """Exit the command-line interpreter."""
        print("Exits the command-line interpreter.")

    def help_quit(self):
        """Exit the command-line interpreter."""
        print("Exits the command-line interpreter.")

    def postloop(self):
        print("Exiting the command-line interpreter. Goodbye!")


if __name__ == "__main__":
    cmd_instance = HBNBCommand()
    cmd_instance.cmdloop()
