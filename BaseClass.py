import pytest
from selenium import webdriver


@pytest.mark.usefixtures('steUp')
class BaseClass:
    pass
