import time

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import allure
import shutil
import errno, os, stat, shutil

#shutil.rmtree("C:\\Users\\Edona Xhemajli\\PycharmProjects\\untitled2\\Reports")

driver = webdriver.Chrome(executable_path = 'C:/Users/Edona Xhemajli/Desktop/chrome/chromedriver.exe')


class NewLead:



    driver.get('http://broker-crm.time2code.ch/')
    driver.maximize_window()

   # def handleRemoveReadonly(func, path, exc):
   #      excvalue = exc[1]
   #      if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
   #          os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # 0777
   #          func(C:/Users/Edona Xhemajli/PycharmProjects/untitled2/Reports)
   #      else:
   #          raise

    def loginForm(self):

        try:
            username = driver.find_element_by_xpath("//*[@id='email']").send_keys("director@director.com")
            password = driver.find_element_by_xpath("//*[@id='Password']").send_keys("Test123@")
            clickButton = driver.find_element_by_xpath("//*[@id='loginForm']/div/div[4]/input").click()
        except:
            print("Login credencials incorrect")

    @pytest.fixture()
    def clickLead(self):

        try:
            leadClick = driver.find_element_by_xpath("//*[@id='navbarSupportedContent']/ul/li[1]/a").click()
        except:
            print("Not clickable or xpath is broken!")


    def addNewLead(self):

        try:
            clickAddNewLead = driver.find_element_by_xpath("//*[@id='content']/div/div/div/div/main/div[2]/div/a").click()
        except:
            print("Xpath is broken")

    def leadTyp(self):

        try:
            leadTypSelect = Select(driver.find_element_by_xpath("//*[@id='LeadTypeId']")).select_by_index(2)
        except:
            print("Xpath is broken")

    def leadCategory(self):

        try:
            leadCategory = Select(driver.find_element_by_xpath("//*[@id='leadCategory']")).select_by_index(1)
        except:
            print("Xpath is broken")

    def firstName(self):

        try:
            firstName = driver.find_element_by_xpath("//*[@id='firstname']").send_keys("loloooo")
        except:
            print("Xpath is broken")

    def lastName(self):

        try:
            lastName = driver.find_element_by_xpath("//*[@id='surname']").send_keys("loooooloooooo")
        except:
            print("Xpath is broken")

    def birthDate(self):

        try:
            birthDate = Select(driver.find_element_by_xpath("//*[@id='vinange']")).select_by_index(55)
        except:
            print("Xpath is broken")

    def phoneNumber(self):

        try:
            phoneNumber = driver.find_element_by_xpath("//*[@id='telephone']").send_keys("12345678")
        except:
            print("Xpath is broken")

    def chooseCanton(self):

        try:
            chooseCanton = Select(driver.find_element_by_xpath("//*[@id='canton']")).select_by_index(2)
        except:
            print("Xpath is broken")

    def choosePostalCode(self):

        try:
            postalCode = driver.find_element_by_xpath("//*[@id='postcode']").send_keys("1234")
        except:
            print("The xpath is broken")

    def choosePlace(self):

        try:
            place = driver.find_element_by_xpath("//*[@id='place']").send_keys("asdasd")
        except:
            print("Xpath is broken")

    def chooseStreet(self):

        try:
            strasse = driver.find_element_by_xpath("//*[@id='address']").send_keys("s")
        except:
            print("Xpath is broken")

    def chooseNr(self):

        try:
            nr = driver.find_element_by_xpath("//*[@id='homeNumber']").send_keys("2")
        except:
            print("Xpath is broken")

    def chooseStellensuche(self):

        try:
            stellenSuche = driver.find_element_by_xpath("//*[@id='jobsearch']").send_keys("ashdhashd")
        except:
            print("Xpath is broken")

    def chooseRetentionPeriod(self):

        try:
            retentionPeriod = driver.find_element_by_xpath("//*[@id='blockingperiod']").send_keys("testtest")
        except:
            print("Xpath is broken")

    def chooseNrOfPersons(self):

        try:
            nrOfPersons = driver.find_element_by_xpath("//*[@id='persons']").send_keys("2")
        except:
            print("Xpath is broken")

    def chooseLifeInsurance(self):

        try:
            lifeInsurance = driver.find_element_by_xpath("//*[@id='life-insurance']").send_keys("ltestltest")
        except:
            print("Xpath is broken")

    def chooseSV(self):

        try:
            sv = driver.find_element_by_xpath("//*[@id='sv']").send_keys("sunny boy")
        except:
            print("Xpath is broken")


    def chooseCarInsurance(self):

        try:
            carInsurance = driver.find_element_by_xpath("//*[@id='car-insurance']").send_keys("caaaaaaaaaaaaaaaaaaaar")
        except:
            print("Xpath is broken")

    def chooseHealthInsurance(self):

        try:
            healthInsurance = driver.find_element_by_xpath("//*[@id='healthinsurance']").send_keys("hashdhashdhasd")
        except:
            print("Xpath is broken")

    def addSomeComment(self):

        try:
            comment = driver.find_element_by_xpath("//*[@id='lead-register']/div/div[18]/div/textarea").send_keys("HSDDDDDDDDDDDDDDDDDASDHASKJDHQIUWhd")
        except:
            print("Xpath is broken")

    def clickSaveButton(self):

        try:
            saveButton = driver.find_element_by_xpath("//*[@id='lead-register']/div/div[19]/div/div[3]/button").click()
        except:
            print("Xpath is broken")

for x in range(10):

    time.sleep(1)


    obj1 = NewLead()
    obj1.loginForm()
    obj1.clickLead()
    obj1.addNewLead()
    obj1.leadTyp()
    obj1.leadCategory()
    obj1.firstName()
    obj1.lastName()
    obj1.birthDate()
    time.sleep(1)
    obj1.phoneNumber()
    obj1.chooseCanton()
    obj1.choosePostalCode()
    time.sleep(1)
    obj1.choosePlace()
    time.sleep(2)
    obj1.chooseStreet()
    obj1.chooseNr()
    obj1.chooseStellensuche()
    obj1.chooseRetentionPeriod()
    obj1.chooseNrOfPersons()
    obj1.chooseLifeInsurance()
    obj1.chooseSV()
    obj1.chooseCarInsurance()
    obj1.chooseHealthInsurance()
    obj1.addSomeComment()
    obj1.clickSaveButton()
