from selenium.webdriver.common.by import By
import time

class BasePage(object):
    # 初始化：接收从外面传进来的 driver
    def __init__(self, driver):
        self.driver = driver

        # 封装基础的定位方法，方便子类调用

    def find_element_by_id(self, locator):
        return self.driver.find_element(By.ID, locator)

    def find_element_class(self, locator):
        return self.driver.find_element(By.CLASS_NAME, locator)

    def find_elements_class(self, locator):
        # 注意：这里是 find_elements (复数)
        return self.driver.find_elements(By.CLASS_NAME, locator)

class LoginPage(BasePage):
    # 页面元素的定位符 (Locators) - 方便管理
    USERNAME_INPUT = "user-name"
    PASSWORD_INPUT = "password"
    LOGIN_BTN = "login-button"
    TITLE_TEXT = "title"

    def login(self, username, password):
        print(f"正在尝试登录... 用户名: {username}")
        self.driver.get('https://www.saucedemo.com/')

        # 调用父类 BasePage 的方法
        self.find_element_by_id(self.USERNAME_INPUT).send_keys(username)
        self.find_element_by_id(self.PASSWORD_INPUT).send_keys(password)
        self.find_element_by_id(self.LOGIN_BTN).click()

        time.sleep(1)  # 等待页面跳转

    def get_login_success_text(self):
        # 获取标题文本并返回，不要在 Page 里做断言，把结果给 main 去判断
        try:
            return self.find_element_class(self.TITLE_TEXT).text
        except:
            return None

class InventoryPage(BasePage):
    ITEM_PRICE_CLASS = "inventory_item_price"

    def get_all_prices(self):
        """
        获取所有商品价格，清洗数据，并返回一个数字列表
        """
        clean_prices = []
        try:
            # 调用父类的 find_elements 方法
            price_elements = self.find_elements_class(self.ITEM_PRICE_CLASS)

            for element in price_elements:
                original_text = element.text
                # 数据清洗
                price_number = float(original_text.replace("$", ""))
                clean_prices.append(price_number)

            return clean_prices
        except Exception as e:
            print(f"获取价格时出错: {e}")
            return []