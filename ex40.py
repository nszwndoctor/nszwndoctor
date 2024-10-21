class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                       "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

"""
为什么创建__init__ 或者别的类函数时需要多加一个self变量？
如果不加self，cheese = 'Frank' 这样的代码就有歧义了，
它指的既可能是实例的cheese 属性，也可能是一个叫cheese 的局部变量。
有了self.cheese = 'Frank' 就清楚地知道这指的是实例的属性self.cheese 。

"""