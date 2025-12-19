# Selenium Python Automation Practice

这是一个基于 Python 和 Selenium 的自动化测试练手项目。
采用了 Page Object Model (POM) 设计模式，对 SauceDemo 网站进行自动化测试。

## 🛠️ 技术栈
- Python 3
- Selenium 4
- Page Object Model (POM)

## 📂 项目结构
- `BasePage.py`: 封装 Selenium 基础操作
- `LoginPage.py`: 登录页面逻辑
- `InventoryPage.py`: 商品列表页逻辑 (包含数据清洗)
- `main.py`: 测试执行入口

## ✅ 已实现功能
1. 自动登录 SauceDemo。
2. 验证登录成功后的标题断言。
3. 抓取所有商品价格，清洗数据('$')并转换为浮点数。
4. 计算商品总价和最高价。

## 🚀 如何运行
1. 克隆项目到本地
2. 运行 `main.py`