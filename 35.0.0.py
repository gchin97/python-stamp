class Date:
    @classmethod
    def is_date_valid(date_string):
        year, month, day = map(int, date_string.split("-"))
        return month<=12 and day <=31
    

class Person:
    def greeting(self):
        print("no")      

class student(Person):
    def study(self)
        print("hello")

james= student()
james.greeting()
james.study()