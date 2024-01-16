import copy


class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **attr):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} ({self.age})'


if __name__ == '__main__':
    try:
        p = Person('John', 25)
        prototype = Prototype()
        prototype.register_object('person', p)

        p1 = prototype.clone('person', age=30)
        print(p1)

        p2 = prototype.clone('person', age=20)
        print(p2)
    except Exception as e:
        print(e)
