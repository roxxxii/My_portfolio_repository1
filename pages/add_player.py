from pages.base_page import BasePage


class AddPlayer(BasePage):
    name_field_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[2]/div/div/input"
    surname_field_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[3]/div/div/input"
    age_field_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[7]/div/div/input"
    main_position_field_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[11]/div/div/input"
    submit_button_xpath = "//*[text()='Submit']"

    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_age(self, age):
        self.field_send_keys(self.age_field_xpath, age)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.main_position_field_xpath, main_position)

    def click_on_the_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)