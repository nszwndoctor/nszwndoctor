from sys import argv
# read the wyss section for how to run this
script, first, second, third = argv

print(">>>> argv=", repr(argv))

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is: ", third)


""""
sys.argv[]是用来获取命令行参数的,
sys.argv[0]表示代码本身文件路径;
比如在CMD命令行输入 “python XXX.py -help",
在cmd窗口中输入文件路径和传递的三个参数 E:/python3anzhuang/lianxi/ex13.py 1 2 3
PS D:\python312>python ex13.py first second third
那么sys.argv[0]就代表“xxx.py”,sys.argv[1] 就代表 -help
导入import,模块modle,库library. 

argv 和input() 有什么不同？
不同点在于用户输入的时机。
如果参数是在用户执行命令时就要输入，那就用argv ，
如果是在脚本运行过程中需要用户输入，那就用input() 。
命令行参数是字符串吗？
是的，就算你在命令行输入的是数字，
你也需要用int() 把它先转成整数，像int(input()) 这样。

"""