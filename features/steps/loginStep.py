from multiprocessing import context
from behave import *
import data
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time





@when('launch chrome browser')
def step(context):
    # context.driver = webdriver.Chrome(ChromeDriverManager().install())

    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))
    context.driver.maximize_window()
   
    context.waitdriver = WebDriverWait(context.driver, 180)
    context.action = ActionChains(context.driver)
    


@then('we visit kynlogin')
def step(context):
    print('Check')
    context.driver.get(data.values["kynurl"])


    
@when('Login using {Platform} platform with {UserName} and {Password}')
def step(context, Platform, UserName, Password):
    print(Platform)

    if (Platform == 'kynapp'):
        
        
        print('kynapp Login initiated')
        userNameField = context.waitdriver.until(EC.visibility_of_element_located(
            (By.XPATH, data.elements["kynusername"])))
        
        userNameField.click()
        userNameField.clear()
        userNameField.send_keys(UserName)
   

        password = context.waitdriver.until(EC.visibility_of_element_located(
            (By.XPATH, data.elements["kynpassword"])))
        password.click()
        password.clear()
        password.send_keys(Password)



@then('clickloginButton')
def step(context):
    elementToWaitTillHomePageLoads = context.waitdriver.until(EC.visibility_of_element_located(
         (By.XPATH, data.elements["loginButton"]))).click()
    time.sleep(10)
    context.driver.save_screenshot('Screenshot/LoginPage.png')
    

@then('clickpushnotification')
def step(context):
    elementToWaitTillHomePageLoads = context.waitdriver.until(EC.visibility_of_element_located(
         (By.XPATH, data.elements["Push Notification"]))).click()
    time.sleep(10)
    context.driver.save_screenshot('Screenshot/notificationPage.png')


@then('clickreport')
def step(context):
    elementToWaitTillHomePageLoads = context.waitdriver.until(EC.visibility_of_element_located(
         (By.XPATH, data.elements["report"]))).click()
    time.sleep(10)
    context.driver.save_screenshot('Screenshot/reportPage.png')

    
@then('clicklocation')
def step(context):
    elementToWaitTillHomePageLoads = context.waitdriver.until(EC.visibility_of_element_located(
         (By.XPATH, data.elements["location"]))).click()
    time.sleep(10)
    context.driver.save_screenshot('Screenshot/locationPage.png')

    
@then('clickcontent')
def step(context):
    elementToWaitTillHomePageLoads = context.waitdriver.until(EC.visibility_of_element_located(
         (By.XPATH, data.elements["content"]))).click()
    time.sleep(10)
    context.driver.save_screenshot('Screenshot/contentPage.png')


        
@then('clicktelekast')
def step(context):
    elementToWaitTillHomePageLoads = context.waitdriver.until(EC.visibility_of_element_located(
         (By.XPATH, data.elements["telekast"]))).click()
    time.sleep(10)
    context.driver.save_screenshot('Screenshot/telekastPage.png')



    
@then('clicklive request')
def step(context):
    elementToWaitTillHomePageLoads = context.waitdriver.until(EC.visibility_of_element_located(
         (By.XPATH, data.elements["live request"]))).click()
    time.sleep(10)
    context.driver.save_screenshot('Screenshot/liverequestPage.png')




@then('click schedule request')
def step(context):
    elementToWaitTillHomePageLoads = context.waitdriver.until(EC.visibility_of_element_located(
         (By.XPATH, data.elements["Schedule request"]))).click()
    time.sleep(10)
    context.driver.save_screenshot('Screenshot/SchedulerequestPage.png')


        
@then('clickuser')
def step(context):
    elementToWaitTillHomePageLoads = context.waitdriver.until(EC.visibility_of_element_located(
         (By.XPATH, data.elements["user"]))).click()
    time.sleep(10)
    context.driver.save_screenshot('Screenshot/userPage.png')


    
@then('click resource')
def step(context):
    elementToWaitTillHomePageLoads = context.waitdriver.until(EC.visibility_of_element_located(
         (By.XPATH, data.elements["Resoure"]))).click()
    time.sleep(10)
    context.driver.save_screenshot('Screenshot/RESOURCEPage.png')


    
@then('click search')
def step(context):
    elementToWaitTillHomePageLoads = context.waitdriver.until(EC.visibility_of_element_located(
         (By.XPATH, data.elements["search"]))).click()
    time.sleep(10)


    
@then('select kynfluencer')
def step(context):
    elementToWaitTillHomePageLoads = context.waitdriver.until(EC.visibility_of_element_located(
         (By.XPATH, data.elements["kynfluencer"]))).click()
    time.sleep(10)
    context.driver.save_screenshot('Screenshot/kynfluencerPage.png')



    
@then('select Kynformer')
def step(context):
    elementToWaitTillHomePageLoads = context.waitdriver.until(EC.visibility_of_element_located(
         (By.XPATH, data.elements["Kynformer"]))).click()
    time.sleep(10)
    context.driver.save_screenshot('Screenshot/KynformerPage.png')



    
@then('select Public')
def step(context):
    elementToWaitTillHomePageLoads = context.waitdriver.until(EC.visibility_of_element_located(
         (By.XPATH, data.elements["Public"]))).click()
    time.sleep(10)
    context.driver.save_screenshot('Screenshot/PublicPage.png')
   











    
    



    




    

