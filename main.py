class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hello, i am {self.name}")


jhon = Person("jhon Smith")
jhon.talk()

bob = Person("Bob Yaho")
bob.talk()


class Robot(Person):
    def power_on(self):
        print("turned on")


robot1 = Robot('optimos')
robot1.power_on()
robot1.talk()