from testpage import OperationsHelper
import logging
import yaml
import time

with open("./Exam/config.yaml") as f:
    testdata = yaml.safe_load(f)
    username = testdata["username"]
    password = testdata["password"]


def test_step1(browser):
    logging.info("Test1 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(username)
    testpage.enter_pass(password)
    testpage.click_login_button()
    assert testpage.get_user_text() == f"Hello, {username}"


def test_step2(browser):
    logging.info("Test2 Starting")
    testpage = OperationsHelper(browser)
    testpage.click_about_link_btn()
    time.sleep(2)
    assert testpage.get_about_title_css() == "32px"
