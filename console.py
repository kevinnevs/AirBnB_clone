#!/usr/bin/python3
"""
Entry point for the console interpret
"""
import cmd
from models.base_model import BaseModel
from models import storage

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

    def do_create(self, line):
        """
        create an object
        """
        if not len(line):
             print("** class name missing **")
             return
        if line not in HBNBCommand.classes:
             print("** class doesn't exist **")
             return
        newObject = eval(line)()
        print(newObject.id)
        newObject.save()

    def do_show(self, line):
        if not len(line):
             print("** class name is missing **")
             return
        strings = line.split()
        if strings[0] not in HBNBCommand.classes:
             print("** class doesn't exist **")
             return
        if len(strings) == 1:
             print("** instance id missing **")
             return
        keyValue = strings[0] + '.' + strings[1]
        if keyValue not in storage.all().keys():
             print("** no instance found **")
        else:
             print(storage.all()[keyValue])

    def do_destroy(self, line):
        if not len(line):
             print("** class name is missing **")
        strings = line.split()
        if strings[0] not in HBNBCommand.classes:
             print("** class doesn't exist **")
             return
        if len(strings) == 1:
             print("** instance id missing **")
             return
        keyValue = strings[0] + '.' + strings[1]
        if keyValue not in storage.all().keys():
             print("** no instance found **")
             return
        del storage.all()[keyValue]
        storage.save()

    def do_all(self, line):
        if not len(line):
             print([obj for obj in storage.all().values()])
             return
        strings = line.split()
        if strings[0] not in HBNBCommand.classes:
             print("** class doesn't exist **")
             return
        print([obj for obj in storage.all().values()
               if strings[0] == type(obj).__name__])

    def do_update(self, line):
        if not len(line):
            print("** class name missing **")
            return
        strings = split(line)
        for string in strings:
            if string.startswith('"') and string.endswith('"'):
                string = string[1:-1]
        if strings[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(strings) == 1:
            print("** instance id missing **")
        keyValue = strings[0] + '.' + strings[1]
        if keyValue not in storage.all().keys():
            print("** no instance found **")
            return
        if len(strings) == 2:
            print("** attribute name missing **")
            return
        if len(strings) == 3:
            print("** value missing **")
            return
        try:
            setattr(storage.all()[keyValue], strings[2], eval(strings[3]))
        except:
            setattr(storage.all()[keyValue], strings[2], strings[3])

if __name__ == '__main__':
    HBNBCommand().cmdloop()
