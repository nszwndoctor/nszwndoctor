# 简单测试代码

def greet(name, is_morning):
    """
    一个简单的问候函数，根据时间决定问候语。
    
    参数:
    name (str): 用户的名字
    is_morning (bool): 是否是早上
    
    返回:
    str: 个性化的问候语
    """
    
    if is_morning:
        greeting = "Good morning, {}!".format(name)
    else:
        greeting = "Hello, {}!".format(name)
        
    return greeting


# 测试部分
name = "世界"  # 可以替换为你的名字
current_time = True  # 如果想模拟下午的时间，把True改为False

print(greet(name, current_time))  # 输出问候语

# 循环测试
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print("当前数字是：", number)

# 判断数字奇偶性
for i in range(10):
    if i % 2 == 0:
        print(f"{i} 是偶数")
    else:
        print(f"{i} 是奇数")

