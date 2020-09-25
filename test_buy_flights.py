from selenium import webdriver
import unittest
from selenium.webdriver.chrome.options import Options
from pageobjects.main_page import MainPage
from pageobjects.search_results_page import SearchResultsPage


class BuyCases(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('start-maximized')
        self.driver = webdriver.Chrome('drivers/chromedriver.exe', options=chrome_options)
        self.driver.get('https://www.orbitz.com')
        self.driver.implicitly_wait(5)
        self.main_page = MainPage(self.driver)
        self.results_page = SearchResultsPage(self.driver)

    def test_1(self):
        self.main_page.click_flight_button()
        self.main_page.input_origin_flight('Chicago')
        self.main_page.input_destination_flight('New York')
        self.main_page.select_departing_day()
        self.main_page.select_october_day(20)
        self.main_page.select_returning_day()
        self.main_page.select_december_day(15)
        self.main_page.select_adults_passengers('2')
        self.main_page.select_children_passengers('1')
        self.main_page.select_child_1_age('7')
        self.driver.save_screenshot('screenshots/flight_selections.png')
        self.main_page.click_search_button()
        self.assertTrue('3' in self.results_page.return_secondary_summary())
        self.assertEqual('10/20/2020', self.results_page.return_departure_date_1())
        try:
            self.assertEqual(self.results_page.return_title_city_text(), 'Select your departure to New York')
            self.driver.save_screenshot('screenshots/search_result_page.png')
        except:
            self.driver.save_screenshot('screenshots/error.png')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()