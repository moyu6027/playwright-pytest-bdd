# -*- coding: utf-8 -*-
# @Author  : sean
# @File    : faker_helper.py
from faker import Faker
from faker.providers import BaseProvider, internet

faker = Faker()


def get_faker_ipv4():
    """
    获取随机IPv4
    :return:
    """
    faker.add_provider(internet)
    return faker.ipv4()


def get_faker_uuid():
    """
        获取随机UUID
        :return:
        """
    faker.add_provider(BaseProvider)
    return faker.uuid4()


def get_faker_int():
    """
    获取随机整数
    :return:
    """
    faker.add_provider(BaseProvider)
    return faker.random_int()


def get_faker_linux_version():
    """
    获取随机版本号
    :return:
    """
    faker.add_provider(BaseProvider)
    return faker.linux_platform_token()


def get_faker_linux_processor():
    """
    获取随机处理器
    :return:
    """
    faker.add_provider(BaseProvider)
    return faker.linux_processor()


def fake_str(length=10):
    """
    获取随机字符串
    :return:
    """
    faker.add_provider(BaseProvider)
    return faker.pystr(min_chars=length, max_chars=length)


print(get_faker_linux_processor())
