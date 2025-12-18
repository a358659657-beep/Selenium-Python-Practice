from selenium import webdriver
from Basepage import *
# 1. 启动浏览器 (Driver 在这里初始化)
driver = webdriver.Chrome()
driver.implicitly_wait(5)

try:
    # ================= 步骤 1: 登录测试 =================
    # 实例化 LoginPage，把 driver 传进去
    login_page = LoginPage(driver)

    # 执行登录动作
    login_page.login("standard_user", "secret_sauce")

    # 获取结果并断言
    title_text = login_page.get_login_success_text()

    if title_text == "Products":
        print("✅ 登录测试通过！")
    else:
        print(f"❌ 登录测试失败，当前标题是: {title_text}")

    # ================= 步骤 2: 价格测试 =================
    # 实例化 InventoryPage，把同一个 driver 传进去
    inventory_page = InventoryPage(driver)

    # 获取价格数据
    prices = inventory_page.get_all_prices()

    print(f"抓取到的价格列表: {prices}")

    # 数据验证逻辑
    if len(prices) == 6:
        print(f"✅ 商品数量正确: {len(prices)}")
        print(f"最高价格是: ${max(prices)}")
        print(f"总价格是: ${sum(prices)}")
    else:
        print("❌ 商品数量不正确")

except Exception as e:
    print(f"测试过程中发生意外错误: {e}")

finally:
    # ================= 收尾工作 =================
    print("测试结束，关闭浏览器。")
    input("按回车键退出...")  # 给你留个时间看结果
    driver.quit()