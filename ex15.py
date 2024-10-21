from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here`s your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())

"""
代码的第1～3行使用argv 来获取文件名，这个你应该已经很熟悉了。
在接下来的第5行我们使用了open 这个新命令。
现在请在命令行运行pydoc open 来读读它的说明。
你可以看到它和你的脚本或者input 命令类似，
它会接收一个参数，并且返回一个值，你可以将这个值赋给一个变量。
这就是你打开文件的过程。
第7行我们打印了一小行，但在第8行我们看到了新奇的东西。
我们在txt 上调用了一个read 函数。
你从open 获得的东西是一个file （文件），文件本身也有一些你给它的命令。
它接收命令的方式是使用句点（.），紧跟着你的命令名，
然后再跟着类似open 和input 的参数。
不同点是：当你说txt.read() 时，
你的意思其实是：“嘿txt ！执行你的read 命令，无须任何参数！”
之前你运行脚本只需要脚本名称，
现在你用了argv，就要添加参数了。

"""
