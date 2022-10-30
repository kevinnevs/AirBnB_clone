#!/usr/bin/python3
"""module console holds the methods for testing the airbnb backend"""
import cmd
import re
from models import storage
from models.new_class import make_class


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"
    allowed = 'BaseModel,User,Review,Place,Amenity,City,State'.split(",")

    def do_create(self, obj):
        """usage: create <obj>.\nCreates and saves the new instance to file"""
        if len(obj) == 0:
            print("** class name missing **")
        else:
            cmd = obj.split()
            if cmd[0] not in self.allowed:
                print("** class doesn't exist **")
            else:
                a = make_class(cmd[0])
                print(a.id)
                storage.save()

    def do_show(self, ob_id):
        """usage: show obj id.\nPrints the __dict__ of the object"""
        cmd = ob_id.split()
        if len(cmd) == 0:
            print("** class name missing **")
        elif cmd[0] not in self.allowed:
            print("** class doesn't exist **")
        elif len(cmd) < 2:
            print("** instance id missing **")
        else:
            key = cmd[0] + '.' + cmd[1]
            if key in storage.all().keys():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, ob_id):
        """usage: destroy <obj> <id>.\nDeletes the instance"""
        cmd = ob_id.split()
        if len(cmd) == 0:
            print("** class name missing **")
        elif cmd[0] not in self.allowed:
            print("** class doesn't exist **")
        elif len(cmd) < 2:
            print("** instance id missing **")
        else:
            key = cmd[0] + '.' + cmd[1]
            if key in storage.all().keys():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, obj):
        """usage: all [obj]\nreturns all saved instances or of type obj"""
        obj_str = []
        if obj:
            if obj in self.allowed:
                pattern = '^' + obj
                for key, value in storage.all().items():
                    if re.match(pattern, key) is None:
                        continue
                    else:
                        obj_str.append(str(value))
                print(obj_str)
            else:
                print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                obj_str.append(str(value))
            print(obj_str)

    def do_update(self, cmd):
        """updates the value of a class attribute"""
        cmd = cmd.split()
        if len(cmd) == 0:
            print("** class name missing **")
        elif cmd[0] not in self.allowed:
            print("** class doesn't exist **")
        elif len(cmd) < 2:
            print("** instance id missing **")
        else:
            key = cmd[0] + '.' + cmd[1]
            if key not in storage.all().keys():
                print("** no instance found **")
            elif len(cmd) < 3:
                print("** attribute name missing **")
            elif len(cmd) < 4:
                print("** value missing **")
            else:
                a = storage.all()[key]
                del storage.all()[key]
                setattr(a, cmd[2], cmd[3])
                storage.new(a)
                a.save()

    def help_update(self):
        """returns the help manual for update command"""
        print("Usage: update <class> <id> <attribute> <value>\
\nchanges value of attribute to a new value and updates time")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
