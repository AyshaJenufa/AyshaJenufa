import time
from actions import Action
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox(executable_path=r'C:\Users\aysha\PycharmProjects\pythonProject1\venv\Lib\site-packages\geckodriver-v0.29.1-win64\geckodriver.exe')
driver.get('https://portal.staging.alertive.com/login')

#wait = WebDriverWait(driver,10)
#To maximize browser window
driver.maximize_window()

#Login page with username and password
driver.find_element_by_name("email").send_keys("jenufaAdmin@alertive.com")
driver.find_element_by_name("password").send_keys("A123456a")
button = driver.find_eleme


nt_by_class_name("MuiButton-label")
button.click()

#Waits to load the page
driver.implicitly_wait(10)
time.sleep(1)
#To close the modal window for a new visitor
driver.find_element_by_class_name('sc-bdVaJa.cYQqRL.sc-bxivhb.eTpeTG.reactour__close').click()
time.sleep(4)

#To open admin tab
driver.find_element_by_class_name('MuiButtonBase-root-246.MuiListItem-root-238.jss283.relative.level-0.dense.MuiListItem-gutters-243.MuiListItem-button-244').click()

#To open organizations
driver.find_element_by_class_name('MuiButtonBase-root-246.MuiListItem-root-238.SEN-mainMenu-organizations-menu-item.jss235.dense.MuiListItem-gutters-243.MuiListItem-button-244').click()
time.sleep(2)
driver.implicitly_wait(10)
#To open Add new organization
driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/div/div[2]/div/div[1]/div/div/button').click()

#To fill the new organizations form
driver.find_element_by_id('name').send_keys("JENUFA CLINIC AUTOMATION")
time.sleep(0.5)
driver.find_element_by_id('phone').send_keys('9384135631')
time.sleep(0.5)
driver.find_element_by_id('primaryContact').send_keys('9234512342')
time.sleep(0.5)
driver.find_element_by_id('address1').send_keys("No 21 Tidel park street")
time.sleep(0.5)
driver.find_element_by_id('city').send_keys('Chennai')
time.sleep(0.5)
driver.find_element_by_id('state-field').click()
time.sleep(0.5)
driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/div/div[2]/div/div[2]/div/form/div/div[8]/div[2]/div/div/select/option[4]').click()
time.sleep(0.5)
driver.find_element_by_id('zip').send_keys('628100')
time.sleep(0.5)
driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/div/div[2]/div/div[2]/div/form/div/div[9]/div[2]/div/div/select').click()
time.sleep(0.5)
driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/div/div[2]/div/div[2]/div/form/div/div[9]/div[2]/div/div/select/option[2]').click()
time.sleep(1)
#To click the create new organization button
driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/div/div[2]/div/div[2]/div/form/div/button').click()
time.sleep(5)
driver.implicitly_wait(40)
#To open Providers
driver.find_element_by_class_name('MuiButtonBase-root-246.MuiListItem-root-238.jss283.relative.level-0.dense.MuiListItem-gutters-243.MuiListItem-button-244').click()
driver.find_element_by_xpath('/html/body/div/div[3]/div/ul/a[1]').click()
time.sleep(2)
#To click Add new providers
driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/div/div[2]/div/div[1]/div/div/a').click()

#To fill Add new providers form
driver.find_element_by_id("firstName").send_keys("JENUFAALERTIVEADMIN")
time.sleep(0.5)
driver.find_element_by_id("lastName").send_keys("AUTOMATION")
time.sleep(0.5)
driver.find_element_by_class_name("MuiButtonBase-root.MuiButton-root.MuiButton-text.MuiPhoneNumber-flagButton").click()
time.sleep(0.5)
driver.find_element_by_class_name("MuiButtonBase-root.MuiListItem-root.MuiMenuItem-root.country.MuiMenuItem-gutters.MuiListItem-gutters.MuiListItem-button").click()
time.sleep(0.5)
driver.find_element_by_name("phoneNumber").send_keys("2123323232")
time.sleep(0.5)
driver.find_element_by_id("emailAddress").send_keys("jenufaAlertiveAdminAutomation@gmail.com")
time.sleep(0.5)
driver.find_element_by_id("role-type-field").click()
time.sleep(0.5)
driver.find_element_by_xpath("/html/body/div/div[1]/div/div/div/div/div[2]/div/div[2]/div/form/div[1]/div[4]/div/div/div/select/option[3]").click()
time.sleep(0.5)
driver.find_element_by_id("test-save-button").click()
time.sleep(12)
driver.implicitly_wait(40)

#To open Patient tab
driver.find_element_by_xpath('/html/body/div/div[1]/div/header[1]/div/div[3]/div/div/div/ul/a[2]').click()
time.sleep(0.5)
#To close patient modal window
driver.find_element_by_class_name('sc-bdVaJa.cYQqRL.sc-bxivhb.eTpeTG.reactour__close').click()
#To click Add new patients
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div/div[2]/div/div[1]/div/div/a').click()
time.sleep(0.5)
driver.find_element_by_id('emailAddress').send_keys('JENUFA_PATIENT_AUTOMATION@gmail.com')
time.sleep(0.5)
driver.find_element_by_name('mobile').send_keys('4323124323')
time.sleep(0.5)
driver.find_element_by_id('firstName').send_keys('Jenufa')
time.sleep(0.5)
driver.find_element_by_id('lastName').send_keys('PatientAutomation')
time.sleep(0.5)
dob = driver.find_element_by_id('test-dob-field')
time.sleep(0.5)
dob.send_keys("2000-08-20")
time.sleep(0.5)
driver.find_element_by_id('test-gender-field').click()
time.sleep(0.5)
driver.find_element_by_css_selector('#test-gender-field > option:nth-child(2)').click()
time.sleep(1)

#To scroll down in a window
#driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/form/div[2]/button[2]').send_keys(Keys.)

driver.execute_script("window.scrollBy(0, 300)")
time.sleep(1)

#To click next button
driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/form/div[2]/button[2]').click()
time.sleep(0.5)
driver.find_element_by_id('addressLine1').send_keys('No 10 North car street,Tidel park')
time.sleep(0.5)
driver.find_element_by_id('zipcode').send_keys('627100')
time.sleep(0.5)
driver.find_element_by_id('city').send_keys('Chennai')
time.sleep(0.5)
driver.find_element_by_id('state-field').click()
time.sleep(0.5)
driver.find_element_by_css_selector('#state-field > option:nth-child(4)').click()
time.sleep(0.5)
driver.find_element_by_id('timezone-field').click()
time.sleep(0.5)
driver.find_element_by_css_selector('option.timezone-option:nth-child(4)').click()
time.sleep(0.5)
#To scroll down the window
driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/form/div[2]/button[2]').send_keys(Keys.PAGE_DOWN)
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/form/div[2]/button[2]').click()
time.sleep(0.5)
driver.find_element_by_id('primary_insurance').click()
time.sleep(0.5)
driver.find_element_by_css_selector('#primary_insurance > option:nth-child(6)').click()
time.sleep(0.5)
driver.find_element_by_id('home-clinic-field').click()
time.sleep(0.5)
driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div[4]/div/div/select/option[29]').click()
time.sleep(0.5)
driver.find_element_by_css_selector('button.MuiButtonBase-root:nth-child(2)').send_keys(Keys.PAGE_DOWN)
time.sleep(0.5)
driver.find_element_by_css_selector('button.MuiButtonBase-root:nth-child(2)').click()
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.find_element_by_id('test-consent-checkbox').click()
driver.find_element_by_id('test-next-button').click()
time.sleep(0.5)
driver.find_element_by_id('password-field').send_keys('A12345678a')
time.sleep(0.5)
driver.find_element_by_id('confirm-password').send_keys('A12345678a')
time.sleep(0.5)
driver.find_element_by_css_selector('button.MuiButtonBase-root:nth-child(2)').click()

