import time

from selenium import webdriver
import os




def CheckAvailable (driver,name):
    driver.implicitly_wait(5)
    try :
        inputName = driver.find_element_by_xpath('//input[@class="form-control input-lg"]')
        inputName.clear()
        time.sleep(1)
        inputName.send_keys(name)
        time.sleep(2)
        driver.find_element_by_xpath("//button[@class='btn btn-lg btn-green']").click()
        time.sleep(2)
        available = driver.find_element_by_xpath("//div[@id='available']").text
        time.sleep(0.5)
        notAvailable = driver.find_element_by_xpath("//div[@id='not-available']").text


        if "available"in available:
            f1 = open("availible.txt","a+")
            f1.write(name)
            print(name + " is available" )
            f1.close()
        if "not"in notAvailable:
            f2 = open("unavailable.txt", "a+")
            f2.write(name)
            print(name + " is not available")
            f2.close()
    except Exception:
        print(str(Exception))
        return


def main():

    path1 = os.getcwd()
    path2 = os.path.join(path1, "chromedriver.exe")
    option = webdriver.ChromeOptions()
    # Removes navigator.webdriver flag

    # For older ChromeDriver under version 79.0.3945.16
    option.add_experimental_option("excludeSwitches", ["enable-automation"])
    option.add_experimental_option('useAutomationExtension', False)
    option.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(path2,options=option)
    driver.get("https://getgamertag.com/")
    driver
    f = open('names.txt','r')
    namesfile = f.readlines()
    f.close()
    for name in namesfile:
        CheckAvailable(driver,name)

    driver.quit()



main()