# ============================================
# Python函数学习指南 - 第二课
# ============================================

# 什么是函数？
# 函数就是一个"工具"，可以重复使用
# 就像你有一个计算器，可以反复使用一样

# ============================================
# 1. 最简单的函数
# ============================================

# 定义一个函数（创建一个工具）
def say_hello():
    print("你好！")

# 使用这个函数（使用这个工具）
say_hello()  # 输出：你好！
say_hello()  # 输出：你好！
say_hello()  # 输出：你好！

# ============================================
# 2. 带参数的函数
# ============================================

# 定义一个带参数的函数
def say_hello_to(name):
    print(f"你好，{name}！")

# 使用函数，传入不同的名字
say_hello_to("小明")  # 输出：你好，小明！
say_hello_to("小红")  # 输出：你好，小红！
say_hello_to("张三")  # 输出：你好，张三！

# ============================================
# 3. 带返回值的函数
# ============================================

# 定义一个计算加法的函数
def add(a, b):
    result = a + b
    return result  # 返回结果

# 使用函数，接收返回值
sum1 = add(5, 3)   # 5 + 3 = 8
sum2 = add(10, 20) # 10 + 20 = 30

print(f"5 + 3 = {sum1}")    # 输出：5 + 3 = 8
print(f"10 + 20 = {sum2}")  # 输出：10 + 20 = 30

# ============================================
# 4. 实际应用：计算器函数
# ============================================

# 定义计算器函数
def calculate(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
    else:
        return "不支持的运算"

# 使用计算器函数
result1 = calculate(10, 5, "+")  # 10 + 5 = 15
result2 = calculate(10, 5, "-")  # 10 - 5 = 5
result3 = calculate(10, 5, "*")  # 10 * 5 = 50
result4 = calculate(10, 5, "/")  # 10 / 5 = 2.0

print(f"10 + 5 = {result1}")
print(f"10 - 5 = {result2}")
print(f"10 * 5 = {result3}")
print(f"10 / 5 = {result4}")

# ============================================
# 5. 实际应用：购物计算函数
# ============================================

# 定义计算总价的函数
def calculate_total(price, quantity):
    total = price * quantity
    return total

# 使用函数计算不同商品的总价
apple_total = calculate_total(5, 2)    # 5元 * 2个 = 10元
orange_total = calculate_total(3, 3)   # 3元 * 3个 = 9元
banana_total = calculate_total(2, 5)    # 2元 * 5个 = 10元

print(f"苹果总价：{apple_total}元")
print(f"橘子总价：{orange_total}元")
print(f"香蕉总价：{banana_total}元")

# ============================================
# 6. 函数的好处
# ============================================

# 不使用函数：代码重复
print("小明")
print("小红")
print("张三")
print("李四")

# 使用函数：代码简洁
def print_name(name):
    print(name)

print_name("小明")
print_name("小红")
print_name("张三")
print_name("李四")

# ============================================
# 练习题
# ============================================

# 练习1：创建一个函数，计算矩形的面积
# 提示：面积 = 长 × 宽
def rectangle_area(length, width):
    area = length * width
    return area

area1 = rectangle_area(10, 5)   # 10 × 5 = 50
area2 = rectangle_area(8, 4)     # 8 × 4 = 32

print(f"长为10，宽为5的矩形面积是：{area1}")
print(f"长为8，宽为4的矩形面积是：{area2}")

# 练习2：创建一个函数，计算圆的面积
# 提示：面积 = π × 半径²
def circle_area(radius):
    pi = 3.14
    area = pi * radius * radius
    return area

area3 = circle_area(5)   # 半径为5的圆的面积
area4 = circle_area(10)  # 半径为10的圆的面积

print(f"半径为5的圆的面积是：{area3}")
print(f"半径为10的圆的面积是：{area4}")

# 练习3：创建一个函数，判断数字是正数、负数还是零
def check_number(num):
    if num > 0:
        return "正数"
    elif num < 0:
        return "负数"
    else:
        return "零"

print(f"5是：{check_number(5)}")
print(f"-3是：{check_number(-3)}")
print(f"0是：{check_number(0)}")
