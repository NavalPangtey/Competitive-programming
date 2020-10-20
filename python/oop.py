
class Employee:

     num_of_emps = 0
     raise_amount = 1.04

     def __init__(self, first,last,pay):  # its like an constructor
     	self.first =first
     	self.last = last
     	self.pay = pay
     	self.email = last+first + '@gmail.com'
        # Employee.num_of_emps += 1

     def fullname(self):                   # it is a class method
        return "{} {} ".format(self.first,self.last)

     def apply_raise(self):
     	self.pay = int(self.pay * self.raise_amount)

     @classmethod
     def set_raise_amount(cls,amount):
     	 cls.raise_amount=amount

     @classmethod
     def from_string(cls,emp_str):
     	first, last, pay = emp_str.split('-')
     	return cls(first,last,pay)

     @staticmethod
     def is_workday(day):
     	if day.weekday()==5 or day.weekday() ==6:
     		return False
     	return True



class Developer(Employee):
	 raise_amount= 1.10
	 def __init__(self,first,last,pay,prog_lang):
	 	super().__init__(first,last,pay)
        #Employee.__init__(self,first,last,pay)
	 	self.prog_lang=prog_lang

class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
	 	super().__init__(first,last,pay)
	    if employees is None :
	        self.employees= []
	    else:
	        self.employees=employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.empr.append(emp)

    def add_remove(self,emp):
        if emp in self.employees:
            self.empr.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('--->',emp.fullname())




dev_1= Developer('naval',"pangtey",50000,'java')
dev_2= Developer('nalini',"moti",60000,'python')
#print(dev_2.raise_amount)

manag_1= Manager('jhon','smith',90000,[dev_1])

print(manag_1.email)

manag_1.add_emp(dev_2)

manag_1.print_emp()



# print(dev_2.prog_lang)

# print(Developer.raise_amount)

#print(emp_1)
#print(emp_2)
# emp_1= Employee('naval',"pangtey",50000)
# emp_2= Employee('nalini',"moti",50000)

# import datetime
# my_date= datetime.date(2020,6,28)
# print(Employee.is_workday(my_date))


# emp_str_1 = 'tanisha-pangtey-100000'
# new_emp_1= Employee.from_string(emp_str_1)

# print(new_emp_1.email)
#print(Employee.num_of_emps)
# emp_1.first = 'naval'
# emp_1.last ="pangtey"
# emp_1.email= 'naval@gmail.com'
# emp_1.pay = 50000

# emp_2.first = 'nalini'
# emp_2.last ="moti"
# emp_2.email= 'nalini@gmail.com'
# emp_2.pay =80000

# print(emp_2.first)
# print(emp_1.email)
#
# print(emp_2.email)
#print(Employee.fullname(emp_1))#in this we have to pass the instance when we call by class name
#class Variables
#Employee.set_raise_amount(1.6)
#emp_2.set_raise_amount(1.6)   # we can aces  it by instances of class

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)



# print(Employee.__dict__)
# print(Employee.__dict__)
# print(emp_2.__dict__)

# emp_2.raise_amount=1.05
# print(emp_2.__dict__)




