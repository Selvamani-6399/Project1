"""
TEST MAIN
"""
from Data import Data
from Locators import Locators

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



class TestOrangeHRM():

    #Fixtures are defined using the @pytest.fixture decorator in Python.
    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(Data.webdata().url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        yield
        self.driver.quit()

    @pytest.mark.html
    def test_successful_employee_login(self,boot):
        # Login to the Webpage using credentials
        try:
            self.driver.find_element(by=By.NAME, value=Locators.WebLocators().usernameLocator).send_keys(Data.webdata().username)
            self.driver.find_element(by=By.NAME, value=Locators.WebLocators().passwordLocator).send_keys(Data.webdata().password)
            self.driver.find_element(by=By.XPATH, value=Locators.WebLocators().buttonLocator).click()
           # Check whether we have loged in to the webpage successfully or not
            expectedurl = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
            curenturl = self.driver.current_url
            if (curenturl == expectedurl):

                print("login successfully")
            else:
                print("Invalid credentials")
        except Exception as e:
            print(f"Exception occurred: {e}")

    @pytest.mark.html
    def test_invalid_employee_login(self,boot):
        # Login to the Webpage using invalid credentials
        try:
            self.driver.find_element(by=By.NAME, value=Locators.WebLocators().usernameLocator).send_keys(
                Data.webdata().username)
            # Provided a invalid password
            self.driver.find_element(by=By.NAME, value=Locators.WebLocators().passwordLocator).send_keys(
                Data.webdata().invalid_password)
            self.driver.find_element(by=By.XPATH, value=Locators.WebLocators().buttonLocator).click()
            # Check whether invalid credentials notification is displayed or not
            if self.driver.find_element(by= By.XPATH, value=Locators.WebLocators().invalid_popup).is_displayed():
                print("Invalid credentials")

            else:
                print("Login successfully")
        except Exception as e:
            print(f"Exception occurred: {e}")

    @pytest.mark.html
    def test_add_new_employee(self,boot):

        # Login in Admin
        try:
            self.driver.find_element(by=By.NAME, value=Locators.WebLocators().usernameLocator).send_keys(
                Data.webdata().username)
            self.driver.find_element(by=By.NAME, value=Locators.WebLocators().passwordLocator).send_keys(
                Data.webdata().password)
            self.driver.find_element(by=By.XPATH, value=Locators.WebLocators().buttonLocator).click()

            # Go to the PIM module
            self.driver.find_element(by=By.XPATH, value=Locators.WebLocators().pim).click()

            # Add a new employee in the PIM
            self.driver.find_element(by=By.XPATH, value=Locators.WebLocators().addbutton).click()
            self.driver.find_element(by=By.NAME, value=Locators.WebLocators().firstnameLocator).send_keys(Data.webdata().firstname)
            self.driver.find_element(by=By.NAME, value=Locators.WebLocators().lastnameLocator).send_keys(Data.webdata().lastname)
            self.driver.find_element(by=By.XPATH, value=Locators.WebLocators().savebtnlocator).click()
            # Check whether Success notification is displayed or not
            success_message =self.driver.find_element(by=By.XPATH, value=Locators.WebLocators().successmassageLocator).text
            print(f"Popup message: {success_message}")
        except Exception as e:
            print(f"Exception occurred: {e}")

    @pytest.mark.html
    def test_edit_new_employee(self,boot):
        # Login as Admin
        try:
            self.driver.find_element(by=By.NAME, value=Locators.WebLocators().usernameLocator).send_keys(
                Data.webdata().username)
            self.driver.find_element(by=By.NAME, value=Locators.WebLocators().passwordLocator).send_keys(
                Data.webdata().password)
            self.driver.find_element(by=By.XPATH, value=Locators.WebLocators().buttonLocator).click()

            # Go to the PIM module
            self.driver.find_element(by=By.XPATH, value=Locators.WebLocators().pim).click()
            # Edit the last name in existing user detail
            self.driver.find_element(by=By.XPATH, value=Locators.WebLocators().editLocator).click()
            self.driver.find_element(by=By.NAME, value=Locators.WebLocators().lastnameLocator).send_keys(Data.webdata().lastname)
            self.driver.find_element(by=By.XPATH, value=Locators.WebLocators().editsavebtnlocator).click()

            # Check whether Success notification is displayed or not
            success_message = self.driver.find_element(by=By.XPATH, value=Locators.WebLocators().successmassageLocator).text
            print(f"Popup message: {success_message}")

        except Exception as e:
            print(f"Exception occurred: {e}")

    @pytest.mark.html
    def test_delete_employee(self,boot):
        #login as Admin
        try:
            self.driver.find_element(by=By.NAME, value=Locators.WebLocators().usernameLocator).send_keys(
                Data.webdata().username)
            self.driver.find_element(by=By.NAME, value=Locators.WebLocators().passwordLocator).send_keys(
                Data.webdata().password)
            self.driver.find_element(by=By.XPATH, value=Locators.WebLocators().buttonLocator).click()

            # Go to the PIM module
            self.driver.find_element(by=By.XPATH, value=Locators.WebLocators().pim).click()
            # Delete the user in the Record
            self.driver.find_element(by=By.XPATH, value=Locators.WebLocators().deleteLocator).click()
            self.driver.find_element(by=By.XPATH, value=Locators.WebLocators().deleteconformationLocator).click()

            # Check whether Success notification is displayed or not
            success_message = self.driver.find_element(by=By.XPATH, value=Locators.WebLocators().successmassageLocator).text
            print(f"Popup message: {success_message}")

        except Exception as e:
            print(f"Exception occurred: {e}")


