import time

from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains




driver = webdriver.Chrome(executable_path='C:/Users/Edona Xhemajli/Desktop/chrome/chromedriver.exe')


class BVC_376:
    driver.get('http://broker-crm.time2code.ch/')
    driver.maximize_window()

    def loginForm(self):

        try:

            username = driver.find_element_by_xpath("//*[@id='email']")
            username.send_keys("admin@admin.com")

            driver.implicitly_wait(1)

            password = driver.find_element_by_xpath("//*[@id='Password']")
            password.send_keys("Test123@")

            driver.implicitly_wait(1)

            buttonClick = driver.find_element_by_xpath("//*[@id='loginForm']/div/div[5]/button")
            buttonClick.click()

        except:

            print("Xpath is broken loginForm")

    def terminFeedback(self):

        try:

            termin = driver.find_element_by_xpath("//*[@id='navbarSupportedContent']/ul/li[2]/a")
            termin.click()

            terminFeedback = driver.find_element_by_xpath("//*[@id='1']/td[15]/a")
            terminFeedback.click()

            hingefahrenClick = driver.find_element_by_xpath(
                "//*[@id='appointmentFeedback']/div/div[1]/div/div/div/div[1]")
            hingefahrenClick.click()

            kundeCC = driver.find_element_by_xpath(
                "//*[@id='appointmentFeedback']/div/div[6]/div/div/div[18]/div/label/span")

            if hingefahrenClick.is_enabled():
                print("Hingefahren is clicked")
            else:
                print("HIngefahren it is not clicked")

            if kundeCC.is_displayed():
                print("Kunden hat durch CC verschohen is displayed")
            else:
                print("Kunden hat durch CC verschohen It is not displayed")

            time.sleep(1)

            kundeCC.click()

            if kundeCC.is_enabled():
                print("Kunden hat durch CC verschohen Is selected")
            else:
                print("It isn't selected")

            date = driver.find_element_by_xpath("//*[@id='followUp_appointment']")

            if date.is_displayed():
                print("Date is displayed")
            else:
                print("Date it is not displayed")

            zeit = driver.find_element_by_xpath("//*[@id='followUp_appointment_time']")

            if zeit.is_displayed():
                print("Zeit it is displayed")
            else:
                print("Zeit it is not displayed")

        except:

            print("Xpath Is broken terminFeedback")






for x in range(100):

    instanceObj1 = BVC_376()

    instanceObj1.loginForm()
    instanceObj1.terminFeedback()