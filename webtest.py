#=================================================#
# Name: WebTest
#
# Abstract: Auto login and do Firmware Update
# 
# Contents:
#
#=================================================#

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.chrome.options import Options
#from test.init import ip
import time
import commands


class WebTest:
    def __init__(self):
        pass

    def WebLoginFWupdate(self,ip):
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument('--headless')
        chrome_options.add_argument('--window-size=1024x768')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        #chrome_options.binary_location = '/usr/bin/chromedriver'
        chrome_options.set_headless()
        driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', chrome_options=chrome_options)
        driver.get("https://"+str(ip)+"/cgi/url_redirect.cgi?url_name=mainmenu")
        time.sleep(1)

        #Login
        inputName = driver.find_element_by_name("name").send_keys("root")
        inputPwd = driver.find_element_by_name("pwd").send_keys("root")
        driver.find_element_by_xpath('//*[@id="pane"]/button').submit()

        #Maximize window
        driver.maximize_window()
        time.sleep(8)

        #Move frame to TOPMENU
        driver.switch_to.frame("TOPMENU")

        #Choose Configuration and Firmware Update
        driver.find_element_by_link_text('Configuration').click()
        time.sleep(2)
        driver.find_element_by_link_text('Firmware Update').click()
        time.sleep(2)

        #Move frame to MainFrame
        driver.switch_to.frame("MainFrame")
        time.sleep(2)

        #Choose firmware Update file
        driver.find_element_by_id('FileBrowse').send_keys("/home/johnnylin/Documents/Supervyse3.5/out/Build.ast2500evb/ast2500evb-si-BMC_FW-Update.bin")

        locator = (By.XPATH,'//*[@id="flot_text_bmc"]')
        try:
            WebDriverWait(driver, 20, 0.5).until(EC.text_to_be_present_in_element(locator,'BMC FW "ast2500evb-si-BMC_FW-Update.bin" had uploaded, please press "Update" to update it.'))

        finally:
            #driver.find_element_by_id('DropBtn').click()    #to drop file
            driver.find_element_by_id('uploadBtn').click()
            time.sleep(120)
            driver.save_screenshot(driver.title+".png")
            driver.quit()
'''
    def WebButtonTest(self):
        
        find_element_by_id("system").click()
        find_element_by_id("side_bar_sys_info").click()
      
        driver.save_screenshot(driver.title+".png")
        
'''
'''
webtest = WebTest(ip)
webtest.WebLoginFWupdate(ip)
'''
