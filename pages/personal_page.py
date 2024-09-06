import time

import allure
from base.base_page import BasePage
from config.link_config import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys


class PersonalPage(BasePage):
    PAGE_URL = Links.PERSONAL_PAGE

    FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")
    SAVE_BUTTON = ("xpath", "(//button[@type='submit'])[1]")
    SPINNER = ("xpath", "//div[@class='oxd-loading-spinner']")

    def change_name(self, new_name):
        """
        Changes the name in the field and saves the new value.
        """
        with allure.step(f"Change name to '{new_name}'"):
            first_name_field = self.wait.until(
                EC.element_to_be_clickable(self.FIRST_NAME_FIELD)
            )
            time.sleep(2)
            first_name_field.send_keys(Keys.COMMAND + "A")
            first_name_field.send_keys(Keys.BACKSPACE)
            time.sleep(2)
            first_name_field.send_keys(new_name)
            self.name = new_name

    @allure.step("Save changes")
    def save_changes(self):
        """
        Clicks the button to save the changes.
        """
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    @allure.step("Verify changes")
    def verify_changes(self):
        """
        Verifies that the changes have been successfully saved.
        """
        self.wait.until(EC.invisibility_of_element_located(self.SPINNER))
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_FIELD))
        self.wait.until(
            EC.text_to_be_present_in_element_value(self.FIRST_NAME_FIELD, self.name)
        )
