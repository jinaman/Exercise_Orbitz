from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SearchResultsPage:
    def __init__(self, my_driver):
        self.driver = my_driver
        self.secondary_summary = (By.XPATH, '//*[@class="secondary-playback-summary"]')
        self.departure_date_1 = (By.ID, 'departure-date-1')
        self.title_city = (By.XPATH, '//*[@data-test-id="title-city-text"]')

    def return_secondary_summary(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.secondary_summary)).text

    def return_departure_date_1(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.departure_date_1)).get_attribute('value')

    def return_title_city_text(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.title_city)).text


