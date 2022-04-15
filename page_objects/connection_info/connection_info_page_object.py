from page_objects.base_page import BasePage
from page_objects.connection_info.connection_info_page_locator import ConnInfoPageLocator
from utils.faker_helper import get_faker_uuid, fake_str


class ConnInfoPageObject(BasePage):

    def go_to_conn_info_page(self):
        self.go_to_url(ConnInfoPageLocator.CONN_INFO_URL)

    def choose_conn_type(self, conn_type):
        locator = f"//span[text()='{conn_type}']"
        if conn_type != 'SNMP':
            self.click(ConnInfoPageLocator.SNMP_TYPE)
            self.click(locator)

    def choose_use_type(self, use_type):
        locator = f"//span[text()='{use_type}']"
        if use_type != '发现采集':
            self.click(ConnInfoPageLocator.DISCOVE_CONN)
            self.click(locator)

    def add_snmp_conn(self, conn_name, port, community, edition, use_type):
        self.click(ConnInfoPageLocator.ADD)
        self.type(ConnInfoPageLocator.NAME, conn_name)
        self.type(ConnInfoPageLocator.PORT, port)
        if edition == 'v2c':
            self.type(ConnInfoPageLocator.READ_ONLY, community)
        self.choose_use_type(use_type)
        self.click(ConnInfoPageLocator.SAVE)

    def delete_conn(self, name):
        locator = f"//*[text()='{name}']/../..//*[text()='删除']"
        self.click(locator)
        self.click(ConnInfoPageLocator.CONFIRM)

    def check_snmp_connection_list(self, name):
        locator = f"//*[text()='{name}']"
        self.go_to_url(ConnInfoPageLocator.CONN_INFO_URL)
        self.is_element_exist(locator)
