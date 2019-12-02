class Student:
  def show_class_name(self):
      print(self.__class__)

a = Student()
a.show_class_name()

class Student2:
  def show_class_name(self):
      print(self.__class__.__name__)

a = Student2()
a.show_class_name()