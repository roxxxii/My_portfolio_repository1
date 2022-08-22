import os
import time
import unittest

from selenium import webdriver

from pages.add_player import AddPlayer
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

class TestAddPlayerForm(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en/players/add')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_fill_in_add_player_form(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        time.sleep(5)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        dashboard_page.click_on_the_add_player_button()
        add_player_form = AddPlayer(self.driver)
        add_player_form.type_in_name('Adam')
        add_player_form.type_in_surname('Kowalski')
        add_player_form.type_in_age('10.10.1989')
        add_player_form.type_in_main_position('bramkarz')
        add_player_form.click_on_the_submit_button()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()