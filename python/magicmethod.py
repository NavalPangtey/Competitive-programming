class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):  # its like an constructor Search Results (__init__ is pronounced “dunder init”: dunder is short for “double-underscore)
        self.first = first
        self.last = last
        self.pay = pay
        self.email = last + first + '@gmail.com'

    def fullname(self):  # it is a class method
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return 'Employee(\'{}\',\'{}\',{})'.format(self.first,self.last,self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(),self.email)

    def __add__(self,other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1= Employee('naval',"pangtey",50000)
emp_2= Employee('nalini',"moti",70000)

# print(emp_1)
# print(repr(emp_1))
# print(str(emp_1))
#
# print(emp_2.__repr__())
# print(emp_2.__str__())

# print(1+2)
# print(int.__add__(1,2))
# print(str.__add__('a','b'))
# print(emp_1+emp_2)

# print(len('test'))
# print('test'.__len__())
print(len(emp_1))
