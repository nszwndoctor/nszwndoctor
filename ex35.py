from sys import exit

def gold_room():
    print("this room is full of gold. how much do you take?")
    
    choice = input(">")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("man, learn to type a number. ")
        
    if how_much < 50:
        print("nice, you`re not greedy, you win!")
        exit(0)
    else:
        dead("you greedy bastard!")
        
        
def bear_room():
    print("there is a bear here. ")
    print("the bear has a bunch of honey. ")
    print("the fat bear is in front of another door")
    print("how are you going to move the bear?")
    bear_moved = False
    
    while True:
        choice = input(">")
        
        if choice == "take honey":
            dead("the bear look at you then slaps you face off. ")
        elif choice == "taunt bear" and not bear_moved:
            print("the bear has moved from the door.")
            print("you can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("the bear gets pissed off and chews you leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("i got no idea what that means.")
            
            
def cthulhu_room():
    print("here you see the great evil Cthulhu.")
    print("he, it, whatever stares at you and you go insane.")
    print("do you flee for your life or eat your head?")
    
    choice = input(">")
    
    if "flee in choice":
        start()
    elif "head" in choice:
        dead("well that was tasty!")
    else:
        cthulhu_room()
        
        
def dead(why):
    print(why, "good job")
    exit(0)
    
def start():
    print("you are in a dark room")
    print("there is a door to your right and left.")
    print("which one do you take?")
    
    choice = input(">")
    
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("you stumble around the room until you starve.")
        
        
start()

"""
为什么你会写while True ？
这样可以创建一个无限循环。

exit(0) 有什么功能？
在很多类型的操作系统里，exit(0) 可以中止某个程序，
而其中的数字参数则用来表示程序是否是遇到错误而中止的。
exit(1) 表示发生了错误，而exit(0) 则表示程序是正常退出的。
这和我们学的布尔逻辑0==False 正好相反，不过你可以用不一样的数字表示不同的错误结果。
比如，你可以用exit(100) 来表示另一种和exit(2) 或exit(1) 不同的错误。

为什么input() 有时写成input('>') ？
input 的参数是一个将会被打印出来的字符串，
这个字符串一般用来提示用户输入。

if 语句的规则
1．每一条if 语句必须包含一个else 。
2．如果这个else 永远都不应该被执行到，因为它本身没有任何意义，
那你必须在else 语句后面使用一个叫die 的函数，让它打印出出错消息并且“死”给你看，
这和上一个习题类似，这样你可以找到很多的错误。
3．if 语句的嵌套不要超过两层，最好尽量保持只有一层。
4．将if 语句当作段落来对待，其中的每一个if 、elif 和
else 组合就跟一个段落的句子组合一样。
在这种组合的最前面和最后面留一个空行以作区分。
5．你的布尔测试应该很简单，如果它们很复杂，你需要在函数
里将它们的运算事先放到一个变量里，并且为变量取一个好名字。

写软件最好的方法是像下面这样一点一点来。
1．在纸上或者索引卡上列出你要完成的任务。这就是你的待办任务。
2．从中挑出最简单的任务。
3．在源代码文件中写下注释，作为你完成任务代码的指南。
4．在注释下面写一些代码。
5．快速运行你的代码，看它是否工作。
6．循环“写代码，运行代码进行测试，修正代码”的过程。
7．从任务列表中划掉这条任务，挑出下一个最简单的任务，重复上述步骤。
这个过程会帮你以系统且一致的方式写出软件来。在工作过程中，
随时更新任务列表，添加新的任务，删除不必要的任务

"""
        