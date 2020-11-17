from selenium import webdriver
import time
import pandas as pd
import config
from webdriver_manager.chrome import ChromeDriverManager
import re

#driver = webdriver.Chrome(ChromeDriverManager().install())

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
#driver.get('https://poslovi.infostud.com/oglasi-za-posao/beograd?education=4&vrste_kategorija_posla=8&working_hours=7&esource=homepage')



#iz main.py
#dodaje link za apliciranje
df = pd.read_csv("spisakposlova.csv")
df["konkurs"] = "https://poslovi.infostud.com/konkurs/"
df.columns = ["Pozicija", "link", "konkurs"]
df['konkurs'] = df['link'].str.extract("(\d\d\d\d\d\d)", expand=True)
df['konkurs'] = 'https://poslovi.infostud.com/konkurs/' + df['konkurs'].astype(str)
df.to_csv("spisakposlova.csv", index=False, header=True)

df = pd.read_csv('spisakposlova.csv')
urls = df['konkurs']

#driver.page_source().contains("Napuštate sajt Poslovi.infostud.com")


for url in urls:
    data = {}
    driver.get(url)

# ne radi
#     if (driver.page_source().contains("Napuštate sajt Poslovi.infostud.com")) is True:
#         driver.close()
# else:


#Vaša prijava je uspešno prosleđena poslodavcu
# if (driver.page_source().contains("Vaša prijava je uspešno prosleđena poslodavcu")) is True:



    cookies = driver.find_element_by_xpath('//*[@id="__allow_ct_container"]/div/div/a')
    cookies.click()

    # cv = driver.find_elements_by_xpath('//*[@id="cv_id_293608"]').click();
    # cv = driver.find_elements_by_xpath('//*[@id="cv_id_293608"]').click();
    cv = driver.find_element_by_css_selector("input[type='radio'][value='293608']")
    cv.click()

    #cover = driver.find_element_by_xpath('//*[@id="__prijava_pp_text_container"]/div/a').click();
    cover = driver.find_element_by_css_selector("input[type='radio'][value='64176']")
    cover.click()
    time.sleep(1)
    #pisi = driver.find_element_by_xpath('*[@id="tinymce"]').click();

    prijava = driver.find_element_by_xpath('//*[@id="__prijava-submit"]')
    prijava.click()
    time.sleep(5)
    konkurisi = driver.find_element_by_xpath('//*[@id="__prijava-preview-submit"]')
    konkurisi.click()

#
# if (driver.page_source().contains("Napuštate sajt Poslovi.infostud.com")){
# driver.close();
# } else{}


    # src = driver.page_source
    # if hasxpath('//*[@id="__prijava-submit"]') == True:
    #     driver.find_element_by_xpath('//*[@id="__prijava-submit"]').click()
    # else:
    #     driver.close()