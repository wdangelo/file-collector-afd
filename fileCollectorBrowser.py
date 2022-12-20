import os
from config import controll_id
from selenium.webdriver import Chrome, Remote
from selenium.webdriver.common.keys import Keys
from time import sleep
from listUrl import list
from utils.emailConfig.email_config import sending
from utils.logs.app import errorLogsIp

from utils.rangedate import tenDaysago

date = tenDaysago.handle()

urls = list()


def execute():

    
    for url in urls:
        
        response = os.system("ping -c 1 " + url.ip)
        
        if response == 0:
            browser = Chrome(executable_path=f"chromedriver")
            #browser = Remote(desired_capabilities={'browserName': 'chrome'})
            browser.maximize_window()
            browser.get(url.url)
            #browser.get("https://10.230.17.205/#page=login")
            sleep(5)
            button_browser_secury = browser.find_element_by_xpath('//*[@id="details-button"]')
            button_browser_secury.click()
            
            button_proceed_to = browser.find_element_by_xpath('//*[@id="proceed-link"]')
            button_proceed_to.click()
            sleep(60)
            
            elem_user_name = browser.find_element_by_name("user_name")
            elem_user_pass = browser.find_element_by_name("password")
            elem_user_name.clear()
            elem_user_pass.clear()
            elem_user_name.send_keys(controll_id["user"])
            elem_user_pass.send_keys(controll_id["password"])
            sleep(2)
            elem_user_name.send_keys(Keys.ENTER)
            sleep(60)
            
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

            error=f"Relógio ponto ip: {url.ip} PA: {url.pa}"
            
            errorLogsIp(error, ip=url.ip)
            print(type(url.ip))
            #sending(error)
        
        continue
            
        print("Coleta de arquivos finalizada")
        

            

if __name__ == '__main__':
    execute()