the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print(f"this is count {number}")
    
# same as above
for fruit in fruits:
    print(f"a fruit of type: {fruit}")
    
# also we can go through mixed lists too
for i in change:
    print(f"i got {i}")
    
# we can also buil lists , first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"adding {i} to the list")
    #append is a function that lists understand
    elements.append(i)
    
# now we can print them out too
for i in elements:
    print(f"Element was: {i}")
    
"""
为什么for i in range(1, 3): 只循环2次而非3次？
range() 函数会从第一个数到最后一个数，但不包含最后一个数。
所以，它到2的时候就停止了，而不会到3。
这种含首不含尾的方式是循环中极其常见的一种用法。

elements.append() 是做什么的？
它的功能是在列表的尾部追加元素。打开Python命令行，
创建几个列表试验一下。以后每次遇到自己不明白的东西，
你都可以在Python shell交互模式试验一下

"""