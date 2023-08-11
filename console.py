#!/usr/bin/python3
"""Implementating the console for the HBnB project."""
import cmd
import shlex
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models


class HBNBCommand(cmd.Cmd):
    """Contains the entry point of the command interpreter."""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exits after receiving the EOF signal."""
        return True

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def help_quit(self):
        """Summary of quit command."""
        print('Quit command to exit the program\n')

    def help_EOF(self):
        """Summary of EOF signal."""
        print('EOF signal to exit the program\n')

    def emptyline(self):
        """Prevents printing anything when an empty line is passed"""
        pass

    def do_create(self, arg):
        """Creates a new instances of BaseModel saves
        it to the JSON file and prints the id.
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            model = eval(arg)()
            model.save()
            print(model.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id.
        """
        arg = arg.split()
        if not arg:
            print("** class name missing **")
            return
        elif arg[0] not in globals():
            print("** class doesn't exist **")
            return
        elif len(arg) < 2:
            print("** instance id missing **")
            return
        else:
            objs = models.storage.all()
            key = arg[0] + "." + arg[1]
            if key in objs:
                print(objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file).
        """
        arg = arg.split()
        if not arg:
            print("** class name missing **")
            return
        elif arg[0] not in globals():
            print("** class doesn't exist **")
            return
        elif len(arg) < 2:
            print("** instance id missing **")
            return
        else:
            objs = models.storage.all()
            key = arg[0] + "." + arg[1]
            if key in objs:
                del(objs[key])
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        """
        objs = models.storage.all()
        if not arg or arg not in globals():
            print("** class doesn't exist **")
            return
        else:
            instances = []
            for key in objs:
                if key.split(".")[0] == arg:
                    instances.append(str(objs[key]))
            if instances:
                print(instances)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        """
        objs = models.storage.all()
        arg = shlex.split(arg)
        if not arg:
            print("** class name missing **")
            return
        elif arg[0] not in globals():
            print("** class doesn't exist **")
            return
        elif len(arg) < 2:
            print("** instance id missing **")
            return
        else:
            key = arg[0] + "." + arg[1]
            if key not in objs:
                print("** no instance found **")
                return
            elif len(arg) < 3:
                print("** attribute name missing **")
                return
            elif len(arg) < 4:
                print("** value missing **")
                return
            else:
                try:
                    attr_type = type(getattr(objs[key], arg[2]))
                    arg[3] = attr_type(arg[3])
                except AttributeError:
                    pass
                setattr(objs[key], arg[2], arg[3])
                objs[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
