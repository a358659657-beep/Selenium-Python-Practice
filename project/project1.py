# 项目 1：自动登录机器人 (复习 Selenium + 基础 Python)
# 任务：
# 打开 SauceDemo 网站。
# 找到用户名输入框，输入 standard_user。
# 找到密码框，输入 secret_sauce。
# 点击登录按钮。
# 关键点（断言）：获取登录后页面左上角的 "Products" 文本，用 Python 的 if 语句判断：如果文字存在，打印“测试通过”；否则打印“测试失败”。
# 应用课程：Web and Mobile Testing with Selenium + Getting Started with Python。
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. 启动浏览器
driver = webdriver.Chrome()

# 设置隐式等待（防止网页加载慢找不到元素，这里设置最长等10秒）
driver.implicitly_wait(10)

try:
    # 2. 打开网站
    print("正在打开网站...")
    driver.get("https://www.saucedemo.com/")

    # 3. 执行登录操作 (这是前置步骤)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 暂停一下，让你能看清登录后的样子（实际工作中不需要）
    time.sleep(2)

    # ==========================================
    # 4. 你的核心任务：获取文本并断言
    # ==========================================

    # 定位页面左上角的标题元素 (在 SauceDemo 中，它的 class 是 'title')
    title_element = driver.find_element(By.CLASS_NAME, "title")

    # 获取元素里的文字
    actual_text = title_element.text
    print(f"获取到的页面标题是: {actual_text}")

    # 使用 Python 的 if 语句进行“断言” (Assertion)
    expected_text = "Products"

    if actual_text == expected_text:
        print("✅ 测试通过！(Test Passed)")
    else:
        print(f"❌ 测试失败！(Test Failed) - 期望是 '{expected_text}'，但实际获取到的是 '{actual_text}'")

except Exception as e:
    # 如果找不到元素或出错，打印错误信息
    print(f"❌ 发生错误: {e}")

# 项目 2：数据驱动的价格验证器 (复习 Access Web Data + Data Structures)
# 任务：
# 登录后，获取页面上所有商品的价格（比如 $29.99, $9.99 等）。
# 数据清洗：利用你学的字符串处理方法，把 $ 符号去掉，把字符串转成 float 类型。
# 存入结构：把商品名和价格存到一个 Python 字典 (Dictionary) 或 列表 (List) 中。
# 逻辑验证：写代码计算这些商品价格的平均值，或者找出最贵的商品打印出来。
# 应用课程：Python Data Structures + Using Python to Access Web Data (解析 HTML 逻辑)。

# 等页面稳一下
time.sleep(2)

print("--- 开始抓取价格 ---")

# ==========================================
# 关键步骤：获取所有价格元素 (注意是 elements)
# ==========================================

# 找到页面上所有 class 名为 'inventory_item_price' 的元素
# 这里的 price_elements 是一个列表 (List)，里面装着很多个 Selenium 元素对象
price_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_price")

# 准备一个空列表，用来存处理好的数字
clean_prices = []

# 3. 循环处理 (Data Extraction & Cleaning)
for element in price_elements:
    # 拿到原始文本，例如 "$29.99"
    original_text = element.text

    # 【数据清洗】去掉 "$" 符号
    # 方法：使用字符串的 replace 方法
    text_without_symbol = original_text.replace("$", "")

    # 【类型转换】转成浮点数 (float)
    price_number = float(text_without_symbol)

    # 存入列表
    clean_prices.append(price_number)

    # 打印一下过程，让你看到发生了什么
    print(f"原始: {original_text} -> 清洗后: {price_number}")

# ==========================================
# 4. 数据验证 (Data Science 简单的应用)
# ==========================================
print("\n--- 数据统计结果 ---")
print(f"抓取到的价格列表: {clean_prices}")

# 计算最高价
max_price = max(clean_prices)
print(f"最贵的商品价格是: ${max_price}")

# 计算总价 (Sum)
total_price = sum(clean_prices)
print(f"所有商品加起来总价是: ${total_price}")

# 断言：验证是否真的抓到了 6 个商品
if len(clean_prices) == 6:
    print("✅ 测试通过：成功抓取到 6 个商品的价格。")
else:
    print(f"❌ 测试失败：商品数量不对，只抓到了 {len(clean_prices)} 个。")

# 结束
input("按回车键关闭...")
driver.quit()


# 项目 3：基于 OOP 的测试框架改造 (复习 Classes and Inheritance —— 最重要的一步)
# 痛点：项目 1 和 2 的代码可能都写在一个 .py 文件里，乱糟糟的。
# 任务：使用 Page Object Model (POM) 设计模式重构代码。
# 创建一个 BasePage 类（Class），把 driver.find_element 这种基础操作封装进去。
# 创建一个 LoginPage 类，继承自 BasePage，里面只写 login() 方法。
# 创建一个 InventoryPage 类，继承自 BasePage，里面只写 get_prices() 方法。
# 新建一个 main.py，实例化这些类来执行测试。
