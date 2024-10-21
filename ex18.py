# this one is like your scripts with argv
def print_two(*args):
    arg1,arg2 = args
    print(f"arg1:{arg1}, arg2:{arg2}")
    
# ok, that *args is actually pointless , we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1:{arg1}, arg2:{arg2}")
    
#this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")
    
# this one takes no arguments
def print_none():
    print("I got nothin`. ")    
    
print_two("zed", "shaw")
print_two_again("zed", "shaw")
print_one("First!")
print_none()

"""
1．首先我们告诉Python我们想使用def 命令创建一个函数，也就是定义 （define）的意思。
2．紧挨着def 的是函数的名字。本例中它的名字是print_two，
但名字可以随便取，叫peanuts 也没关系，但最好函数名能够体现出函数的功能。
3．然后告诉函数，我们需要*args ，这和脚本的argv 非常相似，
参数必须放在圆括号（() ）中才能正常工作。
4．接着用冒号（: ）结束这一行，然后开始下一行缩进。
5．冒号以下，使用4个空格缩进的行都是属于print_two 这个函数的内容。
其中第一行的作用是将参数解包，这和脚本参数解包的原理差不多。

*args 里的* 是什么意思？
它的功能是告诉Python把函数的所有参数都接收进来，然后放到名叫args 的列表中去。
和一直在用的argv 差不多，只不过前者是用在函数上。
如果没什么特殊需要，我们一般不会经常用到这个东西。


"""
