formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "try your",
    "own text here",
    "maybe a poem",
    "or a song about fear"
))


"""
当你看到formatter.format(...) 的时候，这相当于我告诉Python做下面的事情。
1．取第1行定义的formatter 字符串。
2．调用它的format 函数，这相当于告诉它执行一个叫format的命令行命令。
3．给format 传递4个参数，这些参数和formatter 变量中的{} 匹配，
相当于将参数传递给了format 这个命令。
4．在formatter 上调用format 的结果是一个新字符串，
其中的{}被4个变量替换掉了，这就是print 现在打印出的结果。
你可以在一组三引号之间放入任意多行文本。或者用\进行转义。
\'表示是个单引号,  \"表示是个双引号,  \n表示换行。\t表示制表符。\r表示回车。
"""

