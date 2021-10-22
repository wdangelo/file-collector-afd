import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from listUrl import list

from utils.rangedate import tenDaysago

date = tenDaysago.handle()


urls = list()


def execute():
    for url in urls:
        
        response = os.system("ping -c 1 " + url.ip)
        
        if response == 0:
            browser = webdriver.Chrome()
            browser.maximize_window()
            browser.get(url.url)
            button_browser_secury = browser.find_element_by_xpath('//*[@id="details-button"]')
            button_browser_secury.click()
            
            button_proceed_to = browser.find_element_by_xpath('//*[@id="proceed-link"]')
            button_proceed_to.click()
            sleep(5)
            
            elem_user_name = browser.find_element_by_name("user_name")
            elem_user_pass = browser.find_element_by_name("password")
            elem_user_name.clear()
            elem_user_pass.clear()
            elem_user_name.send_keys("admin")
            elem_user_pass.send_keys("admin")
            sleep(2)
            elem_user_name.send_keys(Keys.ENTER)
            sleep(5)
            
            element_button_afd = browser.find_element_by_xpath('//*[@id="MasterPage_menu"]/div/ul/li[4]/a')
            element_button_afd.click()
            sleep(3)
            
            elemment_button_initial_date = browser.find_element_by_xpath('//*[@id="MasterPage_menu"]/div/ul/li[4]/ul/li[3]/a')
            elemment_button_initial_date.click()
            sleep(2)
            
            date_initial_afd = browser.find_element_by_xpath('//*[@id="initial_date"]')
            date_initial_afd.clear()
            date_initial_afd.send_keys(date)
            sleep(2)
            date_initial_afd.send_keys(Keys.ENTER)
            sleep(10)
            browser.close()
            
        else:
            pass
            
        print("Coleta de arquivos finalizada")
        

            

if __name__ == '__main__':
    execute()