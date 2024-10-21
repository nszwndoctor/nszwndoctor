i = 0
numbers = []

while i < 6:
    print(f"at the top i is {i}")
    numbers.append(i)
    
    i = i + 1
    print("Numbers now: ", numbers)
    print(f"at the bottom i is {i}")
    
print("the numbers: ")

for num in numbers:
    print(num)
    
    
"""
概念——while 循环。只要循环语句中的布尔值为True ，
while 循环就会不停地执行它下面的代码块。
它所做的和if 语句类似，也是去检查一个布尔表达式的真假，
不一样的是它下面的代码块不是只被执行一次，
而是执行完后再跳回到while 的顶部，如此重复进行，直到表达式为False 为止。
while 循环有一个问题，那就是有时它会永远无法停止。
为了避免这样的问题，你需要遵循下面的规则。
1．尽量少用while 循环，大部分时候for 循环是更好的选择。
2．重复检查你的while 语句，确定你测试的布尔表达式最终会变成False 。
3．如果不确定，就在while 循环的开始和结尾打印出你要测试的值，看看它的变化。

for 循环和while 循环有何不同？
for 循环只能对一些东西的集合进行循环，while 循环可以对任何对象进行循环。
然而，相比起来while 循环更难弄对，而一般的任务用for 循环更容易一些。

当循环开始时，它会运行整个代码块，代码块结束后跳回到循环的顶部。
如果想把整个过程可视化，可以在循环的各处加入print 语句，用来追踪变量的变化过程。
你可以在循环之前、循环的第一句、循环中间及循环结尾都放一些print 语句，
研究最后的输出，并试着理解循环的工作过程。


"""