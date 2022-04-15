"""As a new-monitor user, feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers,
)

from page_objects.login_page.login_page_object import LoginPage
from utils.bdd_helper import BddHelper


@scenario("login_with_username_password.feature", 'Sean 进行登录操作')
def test_login():
    """Sean 进行登录操作."""
    pass


@scenario("login_with_username_password.feature", 'I want to open the login page,So that I can login to my account.')
def test_login_page():
    """Sean 打开登录页面."""
    pass


@given('Sean 打开新监控网站首页')
def open_new_monitor_home_page(page):
    """Sean 打开新监控网站首页."""
    LoginPage(page).open_site()


@when('Sean 输入用户名和密码登录')
def input_username_password_login(page):
    """Sean 输入用户名和密码登录."""
    LoginPage(page).input_username_password_login()


@then('Sean 可以进入监控面板')
def is_dashboard_present(page):
    """Sean 可以进入监控面板."""
    LoginPage(page).is_login_successful()


@then(parsers.parse('I can see the {content} in login page.'))
def is_login_present(page, content):
    """Sean 可以看到新监控首页."""
    LoginPage(page).is_login_present(content)
