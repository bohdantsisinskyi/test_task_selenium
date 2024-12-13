import os

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from dotenv import load_dotenv

load_dotenv()

URLS = ("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#onboarding/welcome",
        "https://app.spotlightprotocol.com/badge", "https://app.spotlightprotocol.com")

USERNAME = "bohdan_test_selenium"
PASSWORD = "It_Is_Test_PASS_96"

elements = [[(By.ID, 'onboarding__terms-checkbox'),
             (By.CLASS_NAME, 'button.btn--rounded.btn-primary'),
             (By.CLASS_NAME,
              'mm-box.mm-text.mm-button-base.mm-button-base--size-lg.mm-button-primary.mm-text--body-md-medium.mm-box--padding-0.mm-box--padding-right-4.mm-box--padding-left-4.mm-box--display-inline-flex.mm-box--justify-content-center.mm-box--align-items-center.mm-box--color-primary-inverse.mm-box--background-color-primary-default.mm-box--rounded-pill'),
             (By.CLASS_NAME, 'form-field__input'),
             (By.CLASS_NAME,
              'mm-box.mm-checkbox__input.mm-box--margin-0.mm-box--margin-right-2.mm-box--display-flex.mm-box--background-color-background-default.mm-box--rounded-sm.mm-box--border-color-border-default.mm-box--border-width-2.box--border-style-solid'),
             (By.CLASS_NAME, 'button.btn--rounded.btn-primary.btn--large.create-password__form--submit-button'),
             (By.CLASS_NAME,
              'mm-box.mm-text.mm-button-base.mm-button-base--size-lg.mm-button-base--block.mm-button-secondary.mm-text--body-md-medium.mm-box--padding-0.mm-box--padding-right-4.mm-box--padding-left-4.mm-box--display-inline-flex.mm-box--justify-content-center.mm-box--align-items-center.mm-box--color-primary-default.mm-box--background-color-transparent.mm-box--rounded-pill.mm-box--border-color-primary-default.box--border-style-solid.box--border-width-1'),
             (By.CLASS_NAME, 'check-box.skip-srp-backup-popover__checkbox.far.fa-square'),
             (By.CLASS_NAME, 'button.btn--rounded.btn-primary'),
             (By.CLASS_NAME,
              'mm-box.mm-text.mm-button-base.mm-button-base--size-lg.mm-button-primary.mm-text--body-md-medium.mm-box--margin-top-6.mm-box--padding-0.mm-box--padding-right-4.mm-box--padding-left-4.mm-box--display-inline-flex.mm-box--justify-content-center.mm-box--align-items-center.mm-box--color-primary-inverse.mm-box--background-color-primary-default.mm-box--rounded-pill'),
             (By.CLASS_NAME, 'button.btn--rounded.btn-primary'),
             (By.CLASS_NAME, 'button.btn--rounded.btn-primary')],
            [(By.CLASS_NAME, 'chakra-link.chakra-button.css-a5bq08'),
             (By.CLASS_NAME, 'chakra-button.css-1ibdgpm'),
             (By.CLASS_NAME,
              'iekbcc0.iekbcc9.ju367v89.ju367v6i.ju367v73.ju367v7o.ju367vo.ju367vt.ju367vv.ju367v8u.ju367v9f.ju367vb1.g5kl0l0._12cbo8i3.ju367v8r._12cbo8i6'),
             (By.CLASS_NAME,
              '.mm-box.mm-text.mm-button-base.mm-button-base--size-lg.mm-button-base--block.mm-button-primary.mm-text--body-md-medium.mm-box--padding-0.mm-box--padding-right-4.mm-box--padding-left-4.mm-box--display-inline-flex.mm-box--justify-content-center.mm-box--align-items-center.mm-box--color-primary-inverse.mm-box--background-color-primary-default.mm-box--rounded-pill'),
             (By.CLASS_NAME, '.button.btn--rounded.btn-primary'),
             (By.CLASS_NAME,
              'iekbcc0.iekbcc9.ju367v77.ju367v7s.ju367v88.ju367v6h.ju367vc6.ju367vt.ju367vv.ju367vm.ju367v8.ju367v2u.ju367v8v.ju367v9i.ju367v2b._12cbo8i3.ju367v8r._12cbo8i4._12cbo8i7'),
             (By.CLASS_NAME,
              '.mm-box.mm-text.mm-button-base.mm-button-base--size-lg.mm-button-base--block.mm-button-primary.mm-text--body-md-medium.mm-box--padding-0.mm-box--padding-right-4.mm-box--padding-left-4.mm-box--display-inline-flex.mm-box--justify-content-center.mm-box--align-items-center.mm-box--color-primary-inverse.mm-box--background-color-primary-default.mm-box--rounded-pill')],
            [(By.CLASS_NAME, 'chakra-button.css-1hz4p4u'),
             (By.CLASS_NAME, 'chakra-input.css-4dqgg2'),
             (By.CLASS_NAME, 'chakra-button.css-10alacb')]]


class Spotlight:
    def __init__(self):
        self.my_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
        self.chrome_options = Options()
        self.chrome_options.add_argument(f"--user-agent={self.my_user_agent}")
        self.chrome_options.add_argument("--disable-web-security")
        self.chrome_options.add_argument("--disable-features=IsolateOrigins,site-per-process")
        self.chrome_options.add_extension('NKBIHFBEOGAEAOEHLEFNKODBEFGPGKNN_12_8_1_0.crx')

        self.service = Service(executable_path='chromedriver.exe')
        self.driver = webdriver.Chrome(service=self.service, options=self.chrome_options)
        self.driver.maximize_window()
        self.turn = False

    def clicking(self, method, value, time_sleep, counter, url):
        if method == 'id':
            element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, value))
            )
            element.click()
            time.sleep(time_sleep)
        elif method == 'class name':
            if url == 0 and (counter == 3 or counter == 4):
                input_fields = self.driver.find_elements(By.CLASS_NAME, value)
                for input_field in input_fields:
                    input_field.send_keys(PASSWORD)
                    input_field.send_keys(Keys.RETURN)
                time.sleep(time_sleep)
            elif url == 2 and (counter == 2 or counter == 3):
                input_fields = self.driver.find_elements(By.CLASS_NAME, value)
                for input_field in input_fields:
                    input_field.send_keys('Test')
                    input_field.send_keys(Keys.RETURN)
                time.sleep(time_sleep)
            elif url == 1 and value[0] == '.':
                script = f"document.querySelector('{value}').click()"
                self.driver.execute_script(script)
                time.sleep(time_sleep)
            else:
                element = WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.CLASS_NAME, value))
                )
                element.click()
                time.sleep(time_sleep)
        elif method == 'name':
            input_field = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.NAME, value))
            )
            if value == 'text' and counter == 10:
                input_field.send_keys(os.getenv('EMAIL'))
            elif value == 'text' and counter == 12:
                input_field.send_keys(os.getenv('USERNAME_TWITTER'))
            elif value == 'password':
                input_field.send_keys(os.getenv('PASSWORD_TWITTER'))
            time.sleep(time_sleep)
        else:
            element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, value))
            )
            element.click()
            time.sleep(time_sleep)

        if len(self.driver.window_handles) > 1 and not self.turn:
            new_window = self.driver.window_handles[-1]
            self.driver.switch_to.window(new_window)
            print(f"Switched to new window: {new_window}")
            if url == 0:
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(2)
            if counter > 1:
                self.turn = True
        elif len(self.driver.window_handles) == 1:
            self.driver.switch_to.window(self.driver.window_handles[0])
            print("Switched back to main window")
            self.turn = False

    def run(self):
        for i in range(len(URLS)):
            self.driver.get(URLS[i])
            time.sleep(2)
            for count, element in enumerate(elements[i]):
                print(count, element)
                self.clicking(element[0], element[1], 2, count, i)


if __name__ == '__main__':
    spot = Spotlight()
    spot.run()
