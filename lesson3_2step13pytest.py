import unittest
from selenium import webdriver

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

browser = webdriver.Chrome()
browser.implicitly_wait(5)


class MyTests(unittest.TestCase):
    def test_on_the_first_site(self):
        browser.get(link1)
        first_name = browser.find_element_by_css_selector(".first_block .form-control.first")
        first_name.send_keys("Dimas")

        second_name = browser.find_element_by_css_selector(".first_block .form-control.second")
        second_name.send_keys("Normas")

        email = browser.find_element_by_css_selector(".first_block .form-control.third")
        email.send_keys("dimas@normas.com")

        submit = browser.find_element_by_css_selector("button.btn.btn-default")
        submit.click()

        actual_text = browser.find_element_by_tag_name("h1")
        actual_text = actual_text.text

        expected_text = "Congratulations! You have successfully registered!"

        self.assertEqual(actual_text, expected_text, "Text Congratulations! You have successfully registered!")

    def test_on_the_second_site(self):
        browser.get(link2)
        first_name = browser.find_element_by_css_selector(".first_block .form-control.first")
        first_name.send_keys("Dimas")

        second_name = browser.find_element_by_css_selector(".first_block .form-control.second")
        second_name.send_keys("Normas")

        email = browser.find_element_by_css_selector(".first_block .form-control.third")
        email.send_keys("dimas@normas.com")

        submit = browser.find_element_by_css_selector("button.btn.btn-default")
        submit.click()

        actual_text = browser.find_element_by_tag_name("h1")
        actual_text = actual_text.text

        expected_text = "Congratulations! You have successfully registered!"

        self.assertEqual(actual_text, expected_text, "Text Congratulations! You have successfully registered!")

if __name__ == "__main__":
    unittest.main()






