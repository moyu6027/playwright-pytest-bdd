import json
from playwright.sync_api import APIResponse
from api_objects.base_api import BaseApi


class TestApiObject(BaseApi):

    def visit_github_project(self):
        """
        Visit the github project page
        """
        response: APIResponse = self.request_get("/moyu6027/playwright-pytest-bdd/overview_actions/main")
        assert response.ok, "Response is not ok"

