#!/usr/bin/python3
"""Implementating the console for the HBnB project."""
import cmd


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
        """Creates a new instances of abseModel saves it to the JSON file and prints the id."""
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
        Prints the string representation of an instance based on the class name and id.
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()

