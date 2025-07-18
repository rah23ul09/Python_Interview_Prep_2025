""" This wrapping of data which cannot be accessed by outside world is called data encapsulation """

class Encapsulation:
    def __init__(self):
        self.__name = ""        # ".__"is used to initialize data private
        self.__marks = 0        # now these two data cannot be access by outside world

    # using setter to set value for variable
    def set_name(self, name):
        self.__name = name

    def set_marks(self, marks):
        self.__marks = marks

    # using getter to get the value of variables
    def get_name(self):
        return self.__name

    def get_marks(self):
        return self.__marks


student = Encapsulation()
student.set_name("Rahul")
student.set_marks(73)

print(f"{student.get_name()} got {student.get_marks()} marks")
