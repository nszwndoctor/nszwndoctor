cars =100
space_in_a_car = 4.0 
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven*space_in_a_car
average_passengers_per_car = passengers/cars_driven
print("there are ",cars,"cars available.")

print("there are only", drivers,"drivers available")

print("there will be", cars_not_driven, "empty cars today")

print("we can transport",carpool_capacity, "people today.")

print("we have", passengers, "to carpool today.")

print("we need to put about", average_passengers_per_car, "in each car.")

# “变量”（variable）。在编程中，变量只不过是用来指代某个东西的名字。
# 程序员通过使用变量名可以让自己的程序读起来更像自然语言。
# 而且因为程序员的记性都不怎么好，变量名可以让他们更容易记住程序的内容。
#  =的作用是将右边的值赋给左边的变量名。
#  ==的作用是检查左右两边的值是否相等。