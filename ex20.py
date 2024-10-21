from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())
# encoding='gbk', errors='ignore',或encoding='utf-8'，或作用binary_
# .decode('utf-8','ignore' ), open('test.txt', encoding='utf-8')
    
def rewind(f):
    f.seek(0)
    
def print_a_line(line_count, f):
    print(line_count, f.readline())
    
current_file = open(input_file)

print("first let`s print the whole file:\n")

print_all(current_file)

print("now let`s rewind, kind of a tape. ")

rewind(current_file)

print("let`s print three lines:")

current_line = 1
print_a_line(current_line, current_file )

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

""" coding=utf-8
def check_charset(file_path):
    import chardet
    with open(file_path, "rb") as f:
        data = f.read(4)
        charset = chardet.detect(data)['encoding']
    return charset
 
your_path = 你的文件路径
with open(your_path, encoding=check_charset(your_path)) as f:
    data = f.read()
    print(data)

readline() 是怎么知道每一行在哪里的？
readline() 里边的代码会扫描文件的每一个字节，直到找到一
个\n 为止，然后它停止读取文件，并且返回此前发现的文件内容。
文件f 会记录每次调用readline() 后的读取位置，
这样它就可以在下次被调用时读取接下来的一行了。
为什么文件里会有间隔空行？
readline() 函数返回的内容中包含文件本来就有的\n ，
而print 在打印时又会添加一个\n ，这样一来就会多出一个空行了。
解决方法是在print 函数中多加一个参数end="" ，这样print 就
不会为每一行多打印\n 出来了。
    
"""