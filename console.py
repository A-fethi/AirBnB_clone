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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
