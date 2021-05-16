import time
from selenium import webdriver
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def browser():
    print("\nstart browser")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser")
    browser.quit()


class TestMy:

    links = ['https://stepik.org/lesson/236895/step/1',
             'https://stepik.org/lesson/236896/step/1',
             'https://stepik.org/lesson/236897/step/1',
             'https://stepik.org/lesson/236898/step/1',
             'https://stepik.org/lesson/236899/step/1',
             'https://stepik.org/lesson/236903/step/1',
             'https://stepik.org/lesson/236904/step/1',
             'https://stepik.org/lesson/236905/step/1']

    message = []

    @pytest.mark.parametrize("link", links)
    def test_1(self, browser, link):
        browser.get(link)

        text_field = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".textarea"))
        )
        text_field.send_keys(str(math.log(int(time.time()))))

        submit_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
        )
        submit_button.click()

        confirmation = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
        )
        confirmation = confirmation.text

        if confirmation != "Correct!":
            self.message.append(confirmation)

        elif confirmation == "Correct!":
            print("\nCorrect!")

        else:
            print("something went wrong with message")

        print("\nthe answer is: ", ''.join(self.message))








