def break_words(stuff):
    """this function will break up words for us."""
    words = stuff.split('')
    return words

def sort_words(words):
    """sorts the words."""
    return sorted(words)

def print_first_word(words):
    """ prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    word = words.pop(-1)
    print(word)
    
def sort_sentence(sentence):
    """takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
def print_first_and_last_sorted(sentence):
    """sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    
"""
函数里什么时候该用print ，什么时候该用return ？
函数的return 会给调用该函数的代码行一个结果。
思路是这样的：函数通过参数接受输入，通过return 返回输出。
print 和它毫无关系，它只是在终端打印输出而已。

"""
    