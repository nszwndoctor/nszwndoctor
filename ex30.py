people = 30
cars = 40 
trucks = 15

if cars > people:
    print("we should take the cars. ")
elif cars < people:
    print("we should not take the cars. ")
else:
    print("we can`t decide. ")
    
if trucks > cars:
    print("that`s too many trucks. ")
elif trucks < cars:
    print("maybe we could take the trucks. ")
else:
    print("we still can`t decide. ")
    
if people > trucks:
    print("alright , let`s just take the trucks. ")
else:
    print("fine, let`s stay home then.")
    
# 如果多个elif 块都是True ，Python会如何处理？
# Python只会运行它遇到的是True 的第一个块，
# 所以只有第一个为True 的块会运行。
    