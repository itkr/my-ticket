from time import sleep
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def main():
    with webdriver.Chrome() as driver:
        driver.get('https://www.google.com')
        search_box = driver.find_element(By.NAME, 'q')
        search_box.send_keys('Python')
        # search_box.send_keys(Keys.RETURN)
        search_box.submit()
        sleep(5)

        driver.save_screenshot('screenshot.png')


if __name__ == '__main__':
    main()

