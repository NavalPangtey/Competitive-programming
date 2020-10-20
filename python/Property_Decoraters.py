class Employee:

    def __init__(self, first, last):  # its like an constructor Search Results (__init__ is pronounced “dunder init”: dunder is short for “double-underscore)
        self.first = first
        self.last = last
        #self.email = last + first + '@gmail.com'
    @property
    def email(self):  # it is a class method
        return "{}.{}@gmail.com".format(self.last, self.first)

    @property
    def fullname(self):  # it is a class method
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    def fullname(self,name):
        first, last = name.split(' ')
        self.first=first
        self.last=last

    @fullname.deleter
    def fullname(self):
        print('Delete name!')
        self.first=None
        self.last=None

emp_1= Employee('naval',"pangtey")
emp_1.fullname='nav pang'

print(emp_1.first)
print(emp_1.email)

print(emp_1.fullname)

del emp_1.fullname
print(emp_1.fullname)
