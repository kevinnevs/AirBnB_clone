#!/usr/bin/python3
"""module console holds the methods for testing the airbnb backend"""
import cmd
import re
from new_class import new_class
from models import storage


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
                a = new_class(cmd[0])
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
            obj_list = storage.all()
            key = cmd[0] + '.' + cmd[1]
            if key in obj_list:
                a_dic = obj_list[key]
                a = new_class(cmd[0], a_dic)
                print(a)
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
            obj_list = storage.all()
            key = cmd[0] + '.' + cmd[1]
            if key in obj_list:
                del obj_list[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, obj):
        """usage: all [obj]\nreturns all saved instances or of type obj"""
        obj_list = storage.all()
        obj_str = []
        if obj:
            if obj in self.allowed:
                pattern = '^' + obj
                for key, value in obj_list.items():
                    if re.match(pattern, key) is None:
                        continue
                    else:
                        instance = new_class(obj, value)
                        obj_str.append(instance.__str__())
                print(obj_str)
            else:
                print("** class doesn't exist **")
        else:
            for key, value in obj_list.items():
                obj = value['__class__']
                instance = new_class(obj, value)
                obj_str.append(instance.__str__())
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
            obj_list = storage.all()
            key = cmd[0] + '.' + cmd[1]
            if key not in obj_list:
                print("** no instance found **")
            elif len(cmd) < 3:
                print("** attribute name missing **")
            elif len(cmd) < 4:
                print("** value missing **")
            else:
                value = obj_list[key]
                try:
                    value[cmd[2]] = cmd[3]
                except Exception:
                    print("** value missing **")
                    return True
                a = new_class(cmd[0], value)
                a.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
