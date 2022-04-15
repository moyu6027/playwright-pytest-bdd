# encoding: utf-8
"""
Base Page Object
"""
import threading
import time
import allure
from playwright.sync_api import TimeoutError as TError
from playwright.sync_api import Page
from playwright.sync_api import expect
from hamcrest import *


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step('Click locator - {locator}')
    def click(self, locator: str):
        self.page.click(locator)

    @allure.step('Check checkbox locator - {locator}')
    def check(self, locator: str):
        self.page.check(locator)

    @allure.step('Uncheck checkbox locator - {locator}')
    def uncheck(self, locator: str):
        self.page.check(locator)

    @allure.step('Hover locator - {locator}')
    def hover(self, locator: str):
        self.page.hover(locator)

    @allure.step('Go to url - {url}')
    def go_to_url(self, url: str):
        self.page.goto(url)
        self.page.wait_for_load_state()

    @allure.step('Type text - {text} into locator - {locator}')
    def type(self, locator: str, text: str):
        self.click(locator)
        self.page.fill(locator, text)

    @allure.step('Select option - {option} in locator - {locator}')
    def select_option(self, locator: str, option: str):
        self.page.select_option(locator, option)

    @allure.step('Is element - {locator} present')
    def is_element_present(self, locator: str) -> bool:
        try:
            self.page.wait_for_selector(locator)
            return True
        except TError:
            return False

    @allure.step('Is element - {locator} hidden')
    def is_element_hidden(self, locator: str) -> bool:
        try:
            self.page.wait_for_selector(locator, state='hidden')
            return True
        except TError:
            return False

    @allure.step('Is element - {locator} visible')
    def is_element_visible(self, locator: str) -> bool:
        try:
            self.page.wait_for_selector(locator, state='visible')
            return True
        except TError:
            return False

    @allure.step('Is element - {locator} exist')
    def is_element_exist(self, locator: str) -> bool:
        try:
            self.page.wait_for_selector(locator)
            return True
        except TError:
            return False

    @allure.step('Contains Text - {locator} has {text}')
    def has_text(self, locator: str, text: str) -> bool:
        try:
            assert_that(self.page.inner_text(locator), contains_string(text))
            return True
        except TError:
            return False

    @allure.step('Contains Text - has {text}')
    def contains_text(self, text: str) -> bool:
        try:
            locator = str("//*" + "[contains(text(), '" + text + "')]")
            assert_that(self.page.inner_text(locator), contains_string(text))
            return True
        except TError:
            return False

    @allure.step('list number - has {text}')
    def list_contain_total(self, text: str) -> bool:
        try:
            locator = str("//*" + "[contains(string(), '共 {text} 条记录')]")
            assert_that(self.page.inner_text(locator), contains_string(text))
            return True
        except TError:
            return False

    @allure.step('Not contains Text - has {text}')
    def not_contains_text(self, text: str) -> bool:
        try:
            locator = str("//*" + "[contains(text(), '" + text + "')]")
            self.page.wait_for_selector(locator, state='hidden')
            return True
        except TError:
            return False

    @allure.step('click_specify {text}')
    def click_specify_text(self, text: str) -> bool:
        try:
            locator = str("//*" + "[contains(text(), '" + text + "')]")
            self.page.click(locator)
            self.page.click(locator)
            return True
        except TError:
            return False

    @allure.step('Sleep {num}')
    def sleep_num(self, num: str):
        threading.Event().wait(int(num))

    @allure.step('Wait_exec {text}')
    def wait_exec_stat(self, text: str) -> None:
        loop = 1
        while self.contains_text(text) is False and loop < 150:
            time.sleep(1.5)
            print(loop)
            loop = loop + 1

    @allure.step('press {locator} {keyboard}')
    def press(self, locator: str, keyboard: str):
        self.page.press(locator, keyboard)

    @allure.step('Contains Text - {locator} has {text}')
    def have_text(self, locator, text) -> None:
        expect(self.page.locator(locator)).to_have_text(text)
