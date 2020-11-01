#!/usr/bin/python3

""" Console Module """

import cmd
import models
import sys


class HBNBCommand(cmd.Cmd):
    """ Class that contains all the methods required to have an interactive
        shell for the specific purpose of the HBNB project.

        Attributes:
            intro (string): The intro message shown when the cmd is called.
            prompt (string): The prompt message shown when requesting an input.
    """

    prompt = "(hbnb) "
    intro = None

    def emptyline(self):
        """ Does nothing when an empty line is passed as argument to the
            prompt.
        """
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves it (to the JSON file)
            and prints the id. Ex: $ create BaseModel
        """
        print(arg)


    def do_EOF(self, arg):
        """ Quit command to exit the program. """
        sys.exit()

    def do_quit(self, arg):
        """ Quit command to exit the program. """
        sys.exit()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
