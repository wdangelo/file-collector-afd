from selenium.webdriver import Chrome
from time import sleep

driver = Chrome()

def execute():
    driver.maximize_window()
    driver.get(f"https://portal.sisbr.coop.br/cas/login?service=https%3a%2f%2fsisbranalitico.sisbr.coop.br%2fsisbranalitico%2fbi%2f%3fperspective%3dhome")
    
    
    input_user = driver.find_element_by_name('username')
    input_password = driver.find_element_by_name('password')
    input_user.clear()
    input_password.clear()

    input_user.send_keys("roborh5042_00")
    input_password.send_keys("@sicoob5042")
    sleep(3)

    captcha = driver.find_element_by_xpath('//*[@id="recaptcha-anchor-label"]')
    captcha.click()

    buttom_confirm = driver.find_element_by_xpath('//*[@id="submitCredential"]')
    buttom_confirm .click()
    

if __name__ == '__main__':
    execute()