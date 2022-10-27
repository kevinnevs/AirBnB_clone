#!/usr/bin/python3

import cmd
import models

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    
    def do_quit(self, line):
        'Quit comand to exit the program'
        return True

    do_EOF = do_quit

if __name__ == '__main__':
    HBNBCommand().cmdloop()
