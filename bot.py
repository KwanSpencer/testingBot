from selenium import webdriver
from config import keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def order(k):

    driver = webdriver.Chrome('./chromedriver')

    driver.get(k['product_url'])

    driver.find_element_by_xpath('//*[@id="product-select"]').click()
    time.sleep(0.7)
    driver.find_element_by_xpath('//*[@id="product-form-2377454813261"]/input').click()
    time.sleep(0.7)
    driver.find_element_by_xpath('//*[@id="head-right"]/a').click()
    time.sleep(0.7)
    driver.find_element_by_xpath('//*[@id="checkout"]').click()
    driver.find_element_by_xpath('//*[@id="checkout_email"]').send_keys(k["email"])
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_first_name"]').send_keys(k["first_name"])
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_last_name"]').send_keys(k["last_name"])
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_address1"]').send_keys(k["address"])
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_address2"]').send_keys(k["flat"])
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_city"]').send_keys(k["city"])
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_zip"]').send_keys(k["postcode"])
    time.sleep(0.1)
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_phone"]').send_keys(k["phone"])
    driver.switch_to_frame(driver.find_element_by_css_selector('iframe'))
    time.sleep(0.3)
    driver.find_element_by_xpath('//*[@class="recaptcha-checkbox-checkmark"]').click()
    #driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[2]/form/div[2]/button')

time.sleep(5    )

if __name__ == '__main__':
    order(keys)
