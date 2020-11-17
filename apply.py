from selenium import webdriver
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException

import config
from webdriver_manager.chrome import ChromeDriverManager

#iz main.py#dodaje link za apliciranje
df = pd.read_csv("spisakposlova.csv")
df["konkurs"] = "https://poslovi.infostud.com/konkurs/"
df.columns = ["Pozicija", "link", "konkurs"]
df['konkurs'] = df['link'].str.extract("(\d\d\d\d\d\d)", expand=True)
df['konkurs'] = 'https://poslovi.infostud.com/konkurs/' + df['konkurs'].astype(str)
df.to_csv("spisakposlova.csv", index=False, header=True)

df = pd.read_csv('spisakposlova.csv')
urls = df['konkurs']


for url in urls:
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://poslovi.infostud.com/prijava?redirect=%2F')
        driver.maximize_window()

        usernamebox = driver.find_element_by_id("Email_login")
        usernamebox.send_keys('milan.krcadinac@gmail.com')

        passbox = driver.find_element_by_id("Password_login")
        passbox.send_keys(config.password)

        loginbutton = driver.find_element_by_xpath('//*[@id="Password_login"]')
        loginbutton.submit()
        time.sleep(3)
        #data = {}
        driver.get(url)

        cookies = driver.find_element_by_xpath('//*[@id="__allow_ct_container"]/div/div/a')
        cookies.click()

        cv = driver.find_element_by_css_selector("input[type='radio'][value='293608']")
        cv.click()

        cover = driver.find_element_by_css_selector("input[type='radio'][value='64176']")
        cover.click()
        time.sleep(1)


        try:
            grad = driver.find_element_by_xpath(
                '//*[@id="__prijava-form"]/div[1]/div[4]/div/div/div[2]/div[1]/div[1]/input')
            grad.click()
            prijava = driver.find_element_by_xpath('//*[@id="__prijava-submit"]')
            prijava.click()
            time.sleep(5)
            konkurisi = driver.find_element_by_xpath('//*[@id="__prijava-preview-submit"]')
            konkurisi.click()
            time.sleep(1)
            driver.close()
        except NoSuchElementException:
            prijava = driver.find_element_by_xpath('//*[@id="__prijava-submit"]')
            prijava.click()
            time.sleep(5)
            konkurisi = driver.find_element_by_xpath('//*[@id="__prijava-preview-submit"]')
            konkurisi.click()
            time.sleep(1)
            driver.close()
    except NoSuchElementException:
        driver.get(url)
        driver.close()




        #
        # driver = webdriver.Chrome(ChromeDriverManager().install())
        # driver.get('https://poslovi.infostud.com/prijava?redirect=%2F')
        # driver.maximize_window()
        #
        # usernamebox = driver.find_element_by_id("Email_login")
        # usernamebox.send_keys('milan.krcadinac@gmail.com')
        #
        # passbox = driver.find_element_by_id("Password_login")
        # passbox.send_keys(config.password)
        #
        # loginbutton = driver.find_element_by_xpath('//*[@id="Password_login"]')
        # loginbutton.submit()
        # time.sleep(3)
        # # data = {}
        # driver.get(url)
        #
        # cookies = driver.find_element_by_xpath('//*[@id="__allow_ct_container"]/div/div/a')
        # cookies.click()
        #
        # cv = driver.find_element_by_css_selector("input[type='radio'][value='293608']")
        # cv.click()
        #
        # cover = driver.find_element_by_css_selector("input[type='radio'][value='64176']")
        # cover.click()
        # time.sleep(1)
        #
        # prijava = driver.find_element_by_xpath('//*[@id="__prijava-submit"]')
        # prijava.click()
        #
        # time.sleep(5)
        # konkurisi = driver.find_element_by_xpath('//*[@id="__prijava-preview-submit"]')
        # konkurisi.click()
        # time.sleep(1)
        #
        # driver.close()



#value="Nastavak konkurisanja"
#text_found = re.search(r'Napuštate sajt Poslovi.infostud.com', src)
#self.assertNotEqual(text_found, None)