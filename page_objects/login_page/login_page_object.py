from page_objects.base_page import BasePage
from page_objects.login_page.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def open_site(self):
        self.go_to_url(LoginPageLocators.ADDRESS)

    def input_username_password_login(self):
        self.type(LoginPageLocators.USERNAME_FIELD, LoginPageLocators.USERNAME)
        self.type(LoginPageLocators.PASSWORD_FIELD, LoginPageLocators.PASSWORD)
        self.click(LoginPageLocators.LOGIN_BUTTON)

    def is_login_present(self, text):
        return self.has_text(LoginPageLocators.HOME_PAGE_MESSAGE, text)
