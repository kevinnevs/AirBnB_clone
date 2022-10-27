#!/usr/bin/python3
"""
Entry point for the console interpret
"""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """
    custom prompt '(hbnb)'
    quit & EOF to end the console
    help commmand to display quit help
    """
    prompt = '(hbnb)'
    
    def do_quit(self, line):
        'Quit comand to exit the program'
        return True

    do_EOF = do_quit

if __name__ == '__main__':
    HBNBCommand().cmdloop()
