from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from crawler.models import ETLE
from datetime import datetime
import time

class ETLECrawler:
    wait_time = 20
    url = "https://www.etlebanten.info/id/check-data"
    fields = ["plate", "machineNumber", "skeletonNumber"]

    def __init__(self):
        self.browser = None

        self.wait_time = 20
        self.url = "https://www.etlebanten.info/id/check-data"
        self.fields = ["plate", "machineNumber", "skeletonNumber"]

    def _inititiate_browser(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.get(self.url)

    def _fill_form(self, data):
        action_chains = ActionChains(self.browser)

        for field in self.fields:
            element = WebDriverWait(self.browser, self.wait_time).until(
                EC.presence_of_element_located((By.ID, field)))
            value = data.get(field, None)

            action_chains.move_to_element(element).click().perform()
            action_chains.move_to_element(element).send_keys(value).perform()

    def _submit_form(self):
        check_button = self.browser.find_element(By.ID, value="check-button")
        check_button.click()

    def _get_result(self, input, starttime):
        time.sleep(1)
        element = WebDriverWait(self.browser, self.wait_time).until(
            EC.presence_of_element_located((By.TAG_NAME, "tbody")))

        row = element.find_element(By.TAG_NAME, "tr")
        cols = row.find_elements(By.TAG_NAME, "td")

        if len(cols) == 1:
            return None

        offense_timestamp = time.strptime(cols[0].get_attribute("innerText"), "%d-%m-%Y %H:%M")
        offense_timestamp = time.strftime("%Y-%m-%d %H:%M:%S", offense_timestamp)
        location = cols[1].get_attribute("innerText")
        offense_type = cols[2].get_attribute("innerText")
        status = cols[3].get_attribute("innerText")

        result = ETLE(
            plate_number=input["plate"], machine_number=input["machineNumber"],
            skeleton_number=input["skeletonNumber"], location=location,
            offense_type=offense_type, status=status,
            offense_timestamp=offense_timestamp, crawl_timestamp=starttime,
        )
        return result

    def _quit_browser(self):
        self.browser.quit()

    def get_tilang_info(self, data):
        starttime = datetime.now()

        self._inititiate_browser()
        self._fill_form(data)
        self._submit_form()

        result = self._get_result(data, starttime)
        self._quit_browser()
        return result
