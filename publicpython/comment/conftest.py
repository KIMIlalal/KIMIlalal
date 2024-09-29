# 设置成一个fixture固件
import pytest

from comment.yaml_util import clear_yaml


@pytest.fixture(scope='function',autouse=True)
def exe_sql():
    print("连接数据库")
    yield
    print("关闭")


@pytest.fixture(scope='session',autouse=True)
def clear():
    clear_yaml()
