#OOPS CONCEPTS
class student: #class creation
    name="Rajeev"
    age=0
    def study(self):
        print("Study 3 Hour")
        self.sleep()
    def sleep(self):
        print("Sleep 1 Hour")
obj = student() # Object instantiation
obj.study() # Accessing class methods
print("--------------------------------------------------INHERITANCE-------------------------------------------------------------------------------")
class a:
    def show(self):
        print("This is Show Method") 
class b(a):
    def demo(self):
        print("Demo Method")   
class c(a):
    pass
class d(b,c) :
    pass
obj=c()
obj.show()
#obj.demo()
print("--------------------------------------------------POLYMORPHISM-------------------------------------------------------------------------------")
def sum (a=0,b=0,c=0):
    print(a+b+c)

sum(10+20+30)
sum(10+20)
sum(10)
''' Polymorphism with Inheritance:
Polymorphism lets us define methods in the child class that have the same name as the methods in the parent class. 
In inheritance, the child class inherits the methods from the parent class. However, it is possible to modify a method in a child class that it has inherited from the parent class.
This is particularly useful in cases where the method inherited from the parent class doesn't quite fit the child class. In such cases, we re-implement the method in the child class.
This process of re-implementing a method in the child class is known as Method Overriding.'''
class bird:
    def intro(self):
        print("There are many types of birds.")
    def fly(self):
        print("Most of the birds can fly but some cannot.")
class sparrow(bird):
    def fly(self):
        print("i can fly")
class ostrich(bird):
    def fly(self):
        print("i can't fly")
obj=sparrow()
obj.fly()
obj1=ostrich()
obj1.fly()
print("--------------------------------------------------ENCAPSULATION-------------------------------------------------------------------------------")
class A:
    __name="abc"
class B(A):
    def show(self):
        print("This is show method",self.name)
obj=B()
obj.show()