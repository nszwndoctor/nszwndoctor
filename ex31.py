print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input(">")

if door == "1":
    print("There`s a giant bear here eating a cheese cake. ")
    print("What do you do ?")
    print("1. take the cake.")
    print("2. scream at the bear.")
    
    bear = input(">")
    
    if bear == "1":
        print("the bear eats your face off. good job")
    elif bear == "2":
        print("the bear eats your legs off. good job")
    else:
        print(f"well, doing {bear} is probably better" )
        print("bear runs away")
elif door == "2":
    print("you stare into the endless abyss at Cthulhu`s retina")
    print("1,blueberrier")
    print("2, yellow jacked clothespins")
    print("3, understanding revolvers yelling melodies")
    
    insanity = input(">")
    
    if insanity == "1" or insanity == "2":
        print("your body survives powered by a mind of jello")
        print("good job")
    else:
        print("the insanity rots your eyes into a pool of muck")
        print("good job")
else:
    print("you stumble around and fall on a knife and die. good job")
    
"""
这里的重点是你可以在if 语句内部再放一个if 语句作为可运行的代码。
这是一个很强大的功能，可以用来创建嵌套的决定，
其中的一个分支将引向另一个分支的子分支。
可以用多个if-else 组合来替代elif 吗？
有时候可以，不过这也取决于if/else 是怎样写的，
而且这样一来Python就需要去检查每一处if/else ，
而不是像if/elif/else一样，只要检查到第一个True 就可以停下来了。
怎样判断一个数是否处于某个值域中？
有两种办法：经典语法是使用1 < x < 10 或1 <= x < 10 ，
用x in range(1, 10) 也可以。

"""