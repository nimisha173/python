# class MySampleClass:
#     def hello(self,n):
#         # create object
#         self.name=n
#         print("hello "+n)
#     def print_name(self):
#         print(self.name)

# x=MySampleClass()
# y=MySampleClass()
# name="miii"
# x.hello(name) 
# y.hello("anand")
# x.print_name() 



# create constructor

class Team:

    # class variable(accss in every object)
    year=2020
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def add_age(self):
        self.age=self.age+1
    def relocate(self,place):
        self.place=place

    def display(self):
        # Team is like class variable
        print("year:"+str(Team.year))
        print("name:"+self.name)
        print("age:"+str(self.age))
        print("place:"+self.place)

    # create class method

    @classmethod
    def add_year(cls):
        cls.year=cls.year+1


    # static method

    @staticmethod
    def welcome():
        print("welcome")
Team.welcome()

x=Team("nimisha",23,"tvm")
y=Team("anu",29,"tvm")




x.display()
y.display()
print("----------------")
Team.year=Team.year+1

x.add_age()
y.add_age()

x.display()
y.display()

print("----------------")
Team.add_year()
x.add_age()
y.add_age()

x.relocate("klm")
y.relocate("kollam")
x.display()
y.display()
