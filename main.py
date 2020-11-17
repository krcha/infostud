from selenium import webdriver
import time
import pandas as pd
import config
from webdriver_manager.chrome import ChromeDriverManager

f = open("spisakposlova.csv", "w")
f.truncate()
f.close()

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://poslovi.infostud.com/prijava?redirect=%2F')
driver.maximize_window()

usernamebox = driver.find_element_by_id("Email_login")
usernamebox.send_keys('milan.krcadinac@gmail.com')

passbox = driver.find_element_by_id("Password_login")
passbox.send_keys(config.password)

loginbutton = driver.find_element_by_xpath('//*[@id="Password_login"]')
loginbutton.submit()
time.sleep(4)
driver.get('https://poslovi.infostud.com/oglasi-za-posao/beograd?education=4&vrste_kategorija_posla=8&working_hours=7&esource=homepage')

items = []

containers = driver.find_elements_by_xpath('//*[@id="__list_jobs"]')

ids = driver.find_elements_by_xpath("//div[starts-with(@id, 'oglas_')]/div[3]/div[1]/h2/a")

for posao in ids:
    pozicija = posao.text
    linkpozicije = posao.get_attribute(('href'))

    pozicija_list = pozicija.split('\n')
    linkpozicije_list = linkpozicije.split('\n')

    dataframe = {'pozicija': pozicija_list, 'link': linkpozicije_list}

    df = pd.DataFrame(dataframe)

    time.sleep(0.05)
    df.to_csv('C:/Github/infostud/spisakposlova.csv', mode='a', index=False, header=False)

    time.sleep(1.5)

driver.get('https://poslovi.infostud.com/oglasi-za-posao/beograd?education=4&vrste_kategorija_posla=8&working_hours=7&page=2')
items = []
containers = driver.find_elements_by_xpath('//*[@id="__list_jobs"]')
ids = driver.find_elements_by_xpath("//div[starts-with(@id, 'oglas_')]/div[3]/div[1]/h2/a")

for posao in ids:
    pozicija = posao.text
    linkpozicije = posao.get_attribute(('href'))
    pozicija_list = pozicija.split('\n')
    linkpozicije_list = linkpozicije.split('\n')
    dataframe = {'pozicija': pozicija_list, 'link': linkpozicije_list}
    df = pd.DataFrame(dataframe)
    time.sleep(0.05)
    df.to_csv('C:/Github/infostud/spisakposlova.csv', mode='a', index=False, header=False)
    time.sleep(2)

driver.get('https://poslovi.infostud.com/oglasi-za-posao/beograd?education=4&vrste_kategorija_posla=8&working_hours=7&page=3')
items = []
containers = driver.find_elements_by_xpath('//*[@id="__list_jobs"]')
ids = driver.find_elements_by_xpath("//div[starts-with(@id, 'oglas_')]/div[3]/div[1]/h2/a")

for posao in ids:
    pozicija = posao.text
    linkpozicije = posao.get_attribute(('href'))
    pozicija_list = pozicija.split('\n')
    linkpozicije_list = linkpozicije.split('\n')
    dataframe = {'pozicija': pozicija_list, 'link': linkpozicije_list}
    df = pd.DataFrame(dataframe)
    time.sleep(0.05)
    df.to_csv('C:/Github/infostud/spisakposlova.csv', mode='a', index=False, header=False)
    time.sleep(2)

driver.get('https://poslovi.infostud.com/oglasi-za-posao/beograd?education=4&vrste_kategorija_posla=8&working_hours=7&page=4')
items = []
containers = driver.find_elements_by_xpath('//*[@id="__list_jobs"]')
ids = driver.find_elements_by_xpath("//div[starts-with(@id, 'oglas_')]/div[3]/div[1]/h2/a")

for posao in ids:
    pozicija = posao.text
    linkpozicije = posao.get_attribute(('href'))
    pozicija_list = pozicija.split('\n')
    linkpozicije_list = linkpozicije.split('\n')
    dataframe = {'pozicija': pozicija_list, 'link': linkpozicije_list}
    df = pd.DataFrame(dataframe)
    time.sleep(0.05)
    df.to_csv('C:/Github/infostud/spisakposlova.csv', mode='a', index=False, header=False)
    time.sleep(2)

driver.get('https://poslovi.infostud.com/oglasi-za-posao/beograd?education=4&vrste_kategorija_posla=8&working_hours=7&page=5')
items = []
containers = driver.find_elements_by_xpath('//*[@id="__list_jobs"]')
ids = driver.find_elements_by_xpath("//div[starts-with(@id, 'oglas_')]/div[3]/div[1]/h2/a")

for posao in ids:
    pozicija = posao.text
    linkpozicije = posao.get_attribute(('href'))
    pozicija_list = pozicija.split('\n')
    linkpozicije_list = linkpozicije.split('\n')
    dataframe = {'pozicija': pozicija_list, 'link': linkpozicije_list}
    df = pd.DataFrame(dataframe)
    time.sleep(0.05)
    df.to_csv('C:/Github/infostud/spisakposlova.csv', mode='a', index=False, header=False)
    time.sleep(2)


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

# for url in urls:
#     data = {}
#     driver.get(url)
#
# cv = driver.find_elements_by_xpath('//*[@id="cv_id_293608"]').click();
# cover = driver.find_elements_by_xpath('//*[@id="__prijava_pp_text_container"]/div/a').click();
# pisi = driver.find_elements_by_xpath('*[@id="tinymce"]').click();
#
# src = driver.page_source
# if hasxpath('//*[@id="__prijava-submit"]') == True:
#             driver.find_element_by_xpath('//*[@id="__prijava-submit"]').click()
# else:
#     driver.close()


