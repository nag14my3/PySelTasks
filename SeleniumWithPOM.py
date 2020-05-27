import pytest

from BaseClass import BaseClass


class SeleniumWithPOM:

    def __init__(self, driver):
        self.driver = driver

    def printing(self):
        print("value")

