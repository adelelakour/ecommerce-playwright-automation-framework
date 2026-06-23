from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class Login(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.login_tab = page.get_by_role("link", name=" Signup / Login")
        self.login_email_address = page.get_by_placeholder("Email Address").first
        self.login_password = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")

        # self.signup_button = page.get_by_role("button", name="Signup")
        # self.signup_name = page.get_by_placeholder("Name")
        # self.signup_email_address = page.get_by_placeholder("Email Address").nth(1)

    def login_valid_credential(self, email, password):
        self.login_tab.click()
        self.login_email_address.fill(email)
        self.login_password.fill(password)
        self.login_button.click()

