import os
import unittest

from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class Test(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_print_nice_words(self):
        print("WELL DONE!!!!!!!!!")

class TestMediumPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://medium.com')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_check_title(self):
        actual_title = self.get_page_title('https://medium.com')
        expected_title = 'Medium – Where good ideas find you.'
        assert actual_title == expected_title

    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title

    @classmethod
    def tearDown(self):
        self.driver.quit()

#class TestAddPlayerFormm(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/pl/players/add')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_check_titlee(self):
        actual_titlee = self.get_page_titlee('https://scouts-test.futbolkolektyw.pl/pl/players/add')
        expected_titlee = 'Add player'
        assert actual_titlee == expected_titlee

    def get_page_titlee(self, url):
        self.driver.get(url)
        return self.driver.title

    @classmethod
    def tearDown(self):
        self.driver.quit()
