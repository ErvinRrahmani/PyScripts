import time


from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path = 'C:/Users/Edona Xhemajli/Desktop/chrome/chromedriver.exe')

# max the window and navigate to the url
driver.maximize_window()
driver.get('http://188.165.118.24/User/Login')

# username login credentials
username = driver.find_element_by_xpath("//div[1]/input[@class='form-control' and 1]")
username.click()
username.send_keys('ikmmzyrtar@mail.com')

# password login credentials
password = driver.find_element_by_xpath("//div[2]/input[@class='form-control' and 1]")
password.click()
password.send_keys("123")

# button login click
loginButton = driver.find_element_by_xpath("//button")
loginButton.click()

# asset click
assetet = driver.find_element_by_xpath("//ul[@class='list-unstyled']/li[1]/a[1]")
assetet.click()

# generate and propose new asset
propozoAssetin = driver.find_element_by_xpath("//ul[@id='sm_expand_7']/li[1]/a[1]")
propozoAssetin.click()

# fill the propozuesi page
institucioni = driver.find_element_by_xpath("//div[2]/div[@class='form-group' and 1]/input[@class='form-control' and 1]")
institucioni.clear()
institucioni.find_element_by_xpath("//div[2]/div[@class='form-group' and 1]/input[@class='form-control' and 1]")
institucioni.send_keys("Instituti i Kosovës për Mbrojtjen e Monumenteve")

# fill the personi kontakues form
personiKontaktues = driver.find_element_by_xpath("//div[3]/div[@class='form-group' and 1]/input[@class='form-control' and 1]")
personiKontaktues.clear()
personiKontaktues.find_element_by_xpath("//div[3]/div[@class='form-group' and 1]/input[@class='form-control' and 1]")
personiKontaktues.send_keys("Unmik")

# fill the address bar form
address = driver.find_element_by_xpath("//div[4]/div[@class='form-group' and 1]/input[@class='form-control' and 1]")
address.clear()
address.find_element_by_xpath("//div[4]/div[@class='form-group' and 1]/input[@class='form-control' and 1]")
address.send_keys("iasdk")

# fill the telephone number
tel = driver.find_element_by_xpath("//div[5]/div[@class='form-group' and 1]/input[@class='form-control' and 1]")
tel.clear()
tel.find_element_by_xpath("//div[5]/div[@class='form-group' and 1]/input[@class='form-control' and 1]")
tel.send_keys("12312123123")

driver.implicitly_wait(10)

# fill the email bar form
email = driver.find_element_by_xpath("//div[6]/div[@class='form-group' and 1]/input[@class='form-control' and 1]")
email.clear()
email.find_element_by_xpath("//div[6]/div[@class='form-group' and 1]/input[@class='form-control' and 1]")
email.click()
email.send_keys("ikmmzyrtar@email.com")

# forward button
button = driver.find_element_by_xpath("//button[@id='next']")
button.click()

driver.implicitly_wait(10)

# Asset Details
emertimi = driver.find_element_by_name("Name")
emertimi.click()
emertimi.send_keys("hashdahsd")

# zgjidh burimin e emertimit te propozuar
emertimi = Select(driver.find_element_by_xpath("//select[@id='asset-name-source']")).select_by_index(4)

# category
category = driver.find_element_by_xpath("//div[2]/div[@class='radio_Options' and 1]/label[@class='text-center' and 1]/span[1]")
category.click()

# Type (lloji/tipi)
wait = WebDriverWait(driver, 10)
type = driver.find_element_by_xpath("//select[@id='assetTypes']")
type.click()
type1 = driver.find_element_by_xpath("//*[@id='assetTypes']/option[8]")
type1.click()

# law status
lawStatus = driver.find_element_by_xpath("//input[@class='temporaryCheckbox']").click()

# next button
nextButton = driver.find_element_by_xpath("//button[@id='next']")
nextButton.click()

# wizard number 3 (Datimi)
wait = WebDriverWait(driver, 10)

# Unique Number form
uniqueNumber = driver.find_element_by_name("NrUniqueDatabase").send_keys("test test")

# Validation number form
validationNumber = driver.find_element_by_name("PreviousApplicationNr").send_keys("tes tessst")

# Historic Period form
historicPeriod = driver.find_element_by_name("HistoricPeriod").send_keys("2000323")

# Century form
century = driver.find_element_by_name("Century").send_keys("V")

# Absolute Date
absoluteDate = driver.find_element_by_xpath("//input[@class='datepicker form-control flatpickr-input form-control input']").click()
absoluteDate1 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/span[17]").click()

nextButtonV = driver.find_element_by_xpath("//button[@id='next']").click()


# Lokacioni
wait = WebDriverWait(driver, 10)

# location
location = driver.find_element_by_name("ActualLocation").send_keys("dhashdahsd")

# spotted place
spottedPlace = driver.find_element_by_name("LocationDiscovered").send_keys("dahsdhqwuhdaiushdqw")

# choose the city
cityPlace = Select(driver.find_element_by_xpath("//select")).select_by_index(2)

# street address
streetAddress = driver.find_element_by_xpath("//div[5]/div[@class='form-group' and 1]/input[@class='form-control' and 1]")
streetAddress.send_keys("hashdahsdhdqoiwdh")

# cadastral zone
cadastralZone = driver.find_element_by_xpath("//div[6]/div[@class='form-group' and 1]/input[@class='form-control' and 1]")
cadastralZone.send_keys("hdahsdhahsdh")

# coordiantes

# latitude
latitude = driver.find_element_by_xpath("//input[@id='latitude']")
latitude.send_keys("23.23")

# longitude
longitude = driver.find_element_by_xpath("//input[@id='longtitude']").send_keys("43.34")

# location submit button
submitLocaion = driver.find_element_by_xpath("//button[@id='next']").click()

# Kriteret
clickbutton = driver.find_element_by_xpath("//*[@id='asset-application-container']/div[2]/div/div[3]/div[1]/button").click()

try:
# JS JQuery script to remove the parent full content page to test the modal
    driver.execute_script("$('.modal-backdrop').remove()")
except:
    print("It's not deleted")

time.sleep(1)
# click lloji i kriterit
selectCriteria = driver.find_element_by_id("criteria-types")
time.sleep(1)
selectCriteria.click()

# choose the selected
addCriteria1 = driver.find_element_by_xpath("//*[@id='criteria-types']/option[4]")
addCriteria1.click()

# pershkrimi i kriterit text-area
textArea = driver.find_element_by_xpath("//*[@id='description']").send_keys("blla blla blla blla blla")

# click ruaj button
ruajButton = driver.find_element_by_xpath("//*[@id='exampleModal']/div/div/div[3]/button")
ruajButton.click()

try:
# remove the classes with JQuery that where snagging the process
    jsScript = driver.execute_script("$('.navbar.navbar-expand.navbar-dar.bg-primary').remove()")
except:
    print("jsScript It's not deleted")

try:
    jsScript1 = driver.execute_script("$('.modal.fade').remove()")
except:
    print("jsScript1 it's not deleted")

# vazhdo button
moveButton = driver.find_element_by_xpath("//button[@id='next']")
moveButton.click()

# Deklerata e Rendesise

try:
# remove the classes with JQuery that where snagging the process
    jsScript2 = driver.execute_script("$('.navbar.navbar-expand.navbar-dark.bg-primary').remove()")
except:
    print("jsScript2 it's not delted")
# send keys to the deklerata e rendesise
deklerataRendesise = driver.find_element_by_xpath("//textarea[@class='form-control']").send_keys("ahdhasiodahoisdhoqiwhd")

try:
    jsScript3 = driver.execute_script("$('.navbar').remove()")
except:
    print("jsScript3 it's not deleted")
# next button
nbutton1 = driver.find_element_by_xpath("//button[@id='next']").click()

wait1 = driver.implicitly_wait(30)

# Pershkrimi i assetit

pershkrimi = driver.find_element_by_name("Description").send_keys("asdasd")

# siperfaqja brenda perimetrit te assetit
siperfaqjaBrendaAssetit = driver.find_element_by_xpath("//div[2]/div[@class='form-group' and 1]/div[@class='input-group' and 1]/input[@class='form-control' and 1]").send_keys("222")

# siperfaqja brenda zones se mbrojtur
siperfaqjaBrendaZonesMbrojtur = driver.find_element_by_xpath("//div[3]/div[@class='form-group' and 1]/div[@class='input-group' and 1]/input[@class='form-control' and 1]").send_keys("1234")

# wait and vazhdo buttoni
wait2 = driver.implicitly_wait(10)

nbutton2 = driver.find_element_by_xpath("//button[@id='next']").click()

# wait implicitly
wait3 = driver.implicitly_wait(15)

# historiku
historiku = driver.find_element_by_name("HistoricalDescription").send_keys("asdasdqwde")

# next button
nbutton3 = driver.find_element_by_xpath("//button[@id='next']").click()

# wait for the next page in the wizard
wait4 = driver.implicitly_wait(10)

# radio group buttons
radioGroup = driver.find_element_by_xpath("//*[@id='asset-application-container']/div[2]/div[2]/div[2]/div/label[1]").click()

# pershkrimi

pershkrimiForm = driver.find_element_by_xpath("//*[@id='asset-application-container']/div[2]/div[2]/div[3]/div/textarea")
pershkrimiForm.send_keys("ahsdhashdiqwhdiuashd")

# next button
nbutton4 = driver.find_element_by_xpath("//*[@id='next']")
nbutton4.click()

# Integriteti

integriteti = driver.find_element_by_xpath("//*[@id='asset-application-container']/div[2]/div[2]/div[2]/div/textarea")
integriteti.send_keys("ashdahshdahsdqiwhdiu")

# next button
bbutton4 = driver.find_element_by_xpath("//*[@id='next']")
bbutton4.click()

wait5 = driver.implicitly_wait(10)

# Pronari

# Lloji pronesise buttons

llojiPronesiseButton = driver.find_element_by_xpath("//*[@id='asset-application-container']/div[2]/div[2]/div[2]/div/label[1]/span")
llojiPronesiseButton.click()

# Pronari
pronariNjoftuar = driver.find_element_by_xpath("//*[@id='asset-application-container']/div[2]/div[3]/div[1]/div/label[1]/span")
pronariNjoftuar.click()

# institucioni
institucioni = driver.find_element_by_xpath("//*[@id='asset-application-container']/div[2]/div[3]/div[2]/div/input")
institucioni.send_keys("ererer")

# telefoni
telefoni = driver.find_element_by_xpath("//*[@id='asset-application-container']/div[2]/div[3]/div[4]/div/input")
telefoni.send_keys("12345678910")

# addressa
adresa = driver.find_element_by_xpath("//*[@id='asset-application-container']/div[2]/div[3]/div[3]/div/input")
adresa.send_keys("ererer")

# email
email1 = driver.find_element_by_xpath("//*[@id='asset-application-container']/div[2]/div[3]/div[5]/div/input")
email1.send_keys("dasdasd@mail.com")


# jsScript remove bg-light class
jsScript4 = driver.execute_script("$('.bg-light').removeClass('modal-open')")

# next button
nbutton5 = driver.find_element_by_xpath("//*[@id='next']")
nbutton5.click()

wait6 = driver.implicitly_wait(10)

# Shftytzuesi

# emri input
emri = driver.find_element_by_xpath("//*[@id='asset-application-container']/div[2]/div[2]/div[2]/div/input")
emri.send_keys("emrimermiermiermierm")

# lloji marrveshjes
llojiMarrveshjes = driver.find_element_by_xpath("//*[@id='asset-application-container']/div[2]/div[2]/div[3]/div/input")
llojiMarrveshjes.send_keys("ashdahshdahsdqwud")

# lloji i perdorimit
llojiPerdorimit = driver.find_element_by_xpath("//*[@id='asset-application-container']/div[2]/div[2]/div[4]/div/input")
llojiPerdorimit.send_keys("dhashdhasdh")

# next button
try:
    nbutton6 = driver.find_element_by_xpath("//*[@id='next']").click()
except:
    print("Error !!!")

# Dokumentacioni
tes222 = driver.find_element_by_xpath("//*[@id='documentType1']").click()
tes2224 = driver.find_element_by_xpath("//*[@id='documentType1']/option[3]").click()

driver.implicitly_wait(2)

dokumentacioniUpload = driver.find_element_by_id("upload-Filesq")

dokumentacioniUpload.send_keys('C:\lololovin.JPG')

filepath = 'C:\lololovin.JPG'

def add_file(self, filepath_to_path):
    filepath = driver.find_element_by_id('upload-Filesq')
    filepath.send_keys(filepath_to_path)


# next button

nbutton6 = driver.find_element_by_xpath("//*[@id='next']")
nbutton6.click()

# Kushtet e perdorimit

kushtetEPerdorimit = driver.find_element_by_xpath("//*[@id='asset-application-container']/div[3]/div[3]/div/label/input")
kushtetEPerdorimit.click()

# next button
nbutton7 = driver.find_element_by_xpath("//*[@id='next']").click()