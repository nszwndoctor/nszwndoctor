"""
1.TrueandTrue
2.False and True
3.1 == 1 and 2 == 1
4."test" == "test"
5.1 == 1 or 2 != 1
6.True and 1 == 1
7.False and 0 != 0
8.True or 1 == 1
9."test"=="testing
10.1 != 0 and 2 == 1
11."test" != "testing"
12."test" == 1
13.not (True and False)
14.not (1 == 1 and 0 != 1)
15.not (10 == 1 or 1000 == 1000)
16.not (1 != 10 or 3 == 4)
17.not ("testing" == "testing" and "Zed" == "Cool Guy")
18.1 == 1 and (not ("testing" == 1 or 1 == 0))
19."chunky" == "bacon" and (not (3 == 4 or 3 == 3))
20.3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))

"""

from sympy import Symbol, cos
x = Symbol('x')
e = 1/cos(x)
print(e.series(x, 0, 10))
# Result
# 1 + x**2/2 + 5*x**4/24 + 61*x**6/720 + 277*x**8/8064 + O(x**10)
# 安装sympy成功

import numpy as np
a = np.array([1, 2, 3, 4, 5])
print(a)
# 显示[1 2 3 4 5]
# 安装 numpy成功
#10月13日安装 pip install matplotlib成功

