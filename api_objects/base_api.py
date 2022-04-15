# encoding: utf-8
"""
Base API Object
"""
import allure
from playwright.sync_api import BrowserContext, APIResponse


class BaseApi:
    def __init__(self, context: BrowserContext):
        self.request_context = context.request

    @allure.step('Get request - {url}')
    def request_get(self, url) -> APIResponse:
        return self.request_context.get(url=url)

    @allure.step('Post request - {url} with {data}')
    def request_post(self, url, data) -> APIResponse:
        return self.request_context.post(url=url, data=data)

    @allure.step('Put request - {url} with {data}')
    def request_put(self, url, data) -> APIResponse:
        return self.request_context.put(url=url, data=data)

    @allure.step('Delete request - {url}')
    def request_delete(self, url) -> APIResponse:
        return self.request_context.delete(url=url)

    @allure.step('Head request - {url}')
    def request_head(self, url) -> APIResponse:
        return self.request_context.head(url=url)

