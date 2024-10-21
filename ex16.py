from sys import argv

script, filename = argv

print(f"We`re going to erase {filename}. ")
print("If you don`t want that, hit CTRL-C(^C). ")
print("If you do want that, hit RETREN. ")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I`m going to ask you for three lines. ")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I`m going  to write these to the file. ")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally , we close it. ")
target.close()

"""
记住以下命令。
close ：关闭文件。跟你的编辑器中的“文件”→“保存”是一个意思。
read ：读取文件的内容。你可以把结果赋给一个变量。
readline ：只读取文本文件中的一行。
truncate ：清空文件，请小心使用该命令。
write('stuff') ：将“stuff”写入文件。
seek(0) ：将读写位置移动到文件开头。

'w' 是什么意思？
它只是一个只有一个字符的特殊字符串，用来表示文件的访问模式。
如果你用了'w' ，那么你的文件就是“写入”（write）模式。
除'w' 以外，我们还有'r' 表示“读取”（read），'a' 表示“追加”（append）。
如果只写open(filename) ，那就使用'r' （只读）模式打开吗？
是的，这是open() 函数的默认行为。

"""
