#!/usr/bin/python3
"""Contains the entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Class containing the command methods"""
    prompt = "(hbnb) "

    def emptyline(self):
        """Overrides the emptyline"""
        pass

    def do_EOF(self, line):
        """Quit command for exiting the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
