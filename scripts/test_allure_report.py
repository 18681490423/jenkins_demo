import allure
import pytest


class TestAllure:

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step(title="测试步骤001")
    def test_func_1(self):
        allure.attach('我是步骤001')
        assert 1


    @allure.severity(allure.severity_level.NORMAL)
    @allure.step(title="测试步骤002")
    def test_func_2(self):
        allure.attach('我是步骤002')
        assert 1

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step(title="测试步骤003")
    def test_func_3(self):
        allure.attach('我是步骤003')
        assert 0
