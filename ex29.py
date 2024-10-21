print("how many people:", end=' ')
people = input()
print("how many cats:", end=' ')
cats = input()
print("how many dogs:", end=' ')
dogs = input()

print("How old are you?", end=' ')

if people < cats:
    print("Too many cats! The world is doomed!")
    
if people > cats:
    print("Not many cats! The world is saved!")
    
if people < dogs:
    print("The world is dry!")
    
if people < dogs:
    print("The world is drooled on !")
        
if people >= dogs:
    print("People are less than or equal to dogs.")
    
if people <= dogs:
    print("People are less than or equal to dogs.")
    
if people == dogs:
    print("People are dogs.")
    
# 如果这个布尔表达式为真，就运行接下来的代码，否则就跳过这一段。
# 行尾的冒号的作用是告诉Python接下来你要创建一个新的代码块，
# 缩进告诉Python这些代码处于该代码块中。
# 这跟你前面创建函数时的冒号是一个道理。
# Python的规则里，只要一行以冒号（: ）结尾，它接下来的内容就应该有缩进。
