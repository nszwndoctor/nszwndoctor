## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass


## Dog is-a Animal
class Dog(Animal):
    def __init__(self, name):
        ## Dog has-a name
        self.name = name


## Cat is-a Animal
class Cat(Animal):
    def __init__(self, name):
        ## Cat has a name
        self.name = name


## Person is-a object
class Person(object):
    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None


## Employee is-a Person
class Employee(Person):
    def __init__(self, name, salary):
        ## Employee has-a name
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary


## Fish is-a object
class Fish(object):
    pass


## Salmon is-a Fish
class Salmon(Fish):
    pass


## Halibut is a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank has-a pet
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()

"""
这些## ?? 注释是做什么用的？
这些注释是供你填空的。你应该在对应的位置填入is-a、has-a的概念。
重读这个习题，看看其他的注释，仔细理解一下我的意思。

这句self.pet = None 有什么用？
确保类的self.pet 属性被设置为默认None 。

super(Employee, self).__init__(name) 是做什么用的？
这是你可以可靠地将父类的__init__ 方法运行起来的方法。
搜索“python 3 super”，看看人们是怎样众说纷纭的。

"""