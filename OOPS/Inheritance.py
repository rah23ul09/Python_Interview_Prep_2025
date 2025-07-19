class Animal:
    def speak(self):
        print("Animal makes different sound")


class Dog(Animal):
    def speak(self):
        print("Dog barks")


a = Animal()
a.speak()

d = Dog()
d.speak()
