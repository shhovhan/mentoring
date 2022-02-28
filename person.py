class Person:
    INSTANCE_COUNT = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

        Person.INSTANCE_COUNT += 1

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    @classmethod
    def get_instance_count(cls):
        return cls.INSTANCE_COUNT

    @classmethod
    def get_name(cls):
        return cls.__getattr__('name')

    def __str__(self):
        return f'{self.name}'


if __name__ == '__main__':
    p1 = Person('Shushan', 30)
    print(Person.INSTANCE_COUNT)
    p2 = Person('Anna', 10)
    print(Person.INSTANCE_COUNT)
    p3 = Person('Lusine', 27)
    print(Person.INSTANCE_COUNT)
    print(p2.INSTANCE_COUNT)
    p1.INSTANCE_COUNT
    print(p1, p2, p3)