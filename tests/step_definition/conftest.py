from pytest_bdd import given
from page_objects.login_page.login_page_object import LoginPage
from rich.console import Console

console = Console()


def pytest_sessionstart():
    """pytest_session_start."""
    console.rule(f"pytest ui start testing")


@given('Sean has logged in')
def sean_has_logged_in(page):
    """Sean has logged in."""
    LoginPage(page).open_site()
    LoginPage(page).input_username_password_login()
    LoginPage(page).is_login_present("Sean")

