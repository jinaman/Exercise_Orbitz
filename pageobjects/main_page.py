from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


class MainPage:
    def __init__(self, my_driver):
        self.driver = my_driver
        self.flight_button = (By.ID, 'tab-flight-tab-hp')
        self.flight_origin_box = (By.ID, 'flight-origin-hp-flight')
        self.select_option_3 = (By.ID, 'aria-option-3')
        self.flight_destination_box = (By.ID, 'flight-destination-hp-flight')
        self.select_option_1 = (By.ID, 'aria-option-1')
        self.departing_date_box = (By.ID, 'flight-departing-wrapper-hp-flight')
        self.returning_date_box = (By.ID, 'flight-returning-wrapper-hp-flight')
        self.calendar_october = (By.XPATH, '//td[@class="datepicker-day-number notranslate"]/button[contains(string(), "October")]')
        self.calendar_december = (By.XPATH, '//td[@class="datepicker-day-number notranslate"]/button[contains(string(),"December")]')
        self.next_month_button = (By.XPATH, '//*[@class="datepicker-paging datepicker-next btn-paging btn-secondary next"]')
        self.adults_passengers = (By.ID, 'flight-adults-hp-flight')
        self.children_passengers = (By.ID, 'flight-children-hp-flight')
        self.child_1_age = (By.ID, 'flight-age-select-1-hp-flight')
        self.submit_button = (By.XPATH, '//*[@data-gcw-change-submit-text="Search"]')

    def click_flight_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.flight_button)).click()

    def input_origin_flight(self, origin):
        self.driver.find_element(*self.flight_origin_box).send_keys(origin)
        self.driver.find_element(*self.select_option_3).click()

    def input_destination_flight(self, destination):
        self.driver.find_element(*self.flight_destination_box).send_keys(destination)
        self.driver.find_element(*self.select_option_1).click()

    def select_departing_day(self):
        self.driver.find_element(*self.departing_date_box).click()

    def select_october_day(self, day):
        day = day - 1
        self.driver.find_elements(*self.calendar_october)[day].click()

    def select_returning_day(self):
        self.driver.find_element(*self.returning_date_box).click()

    def select_december_day(self, day):
        day = day - 1
        self.driver.find_element(*self.next_month_button).click()
        self.driver.find_element(*self.next_month_button).click()
        self.driver.find_elements(*self.calendar_december)[day].click()

    def select_adults_passengers(self, number):
        value = Select(self.driver.find_element(*self.adults_passengers))
        value.select_by_value(number)

    def select_children_passengers(self, number):
        value = Select(self.driver.find_element(*self.children_passengers))
        value.select_by_value(number)

    def select_child_1_age(self, number):
        value = Select(self.driver.find_element(*self.child_1_age))
        value.select_by_value(number)

    def click_search_button(self):
        self.driver.find_element(*self.submit_button).click()








