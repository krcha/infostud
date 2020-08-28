from selenium import webdriver
import time
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

f = open("spisakposlova.csv", "w")
f.truncate()
f.close()

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://poslovi.infostud.com/prijava?redirect=%2F')

usernamebox = driver.find_element_by_id("Email_login")
usernamebox.send_keys('milan.krcadinac@gmail.com')

passbox = driver.find_element_by_id("Password_login")
passbox.send_keys('pass')

loginbutton = driver.find_element_by_xpath('//*[@id="Password_login"]')
loginbutton.submit()
time.sleep(5)
driver.get('https://poslovi.infostud.com/oglasi-za-posao/beograd?education=4&vrste_kategorija_posla=8&working_hours=7&esource=homepage')



items = []

containers = driver.find_elements_by_xpath('//*[@id="__list_jobs"]')

#radi
ids = driver.find_elements_by_xpath("//div[starts-with(@id, 'oglas_')]/div[3]/div[1]/h2/a")
#firma = driver.find_element_by_xpath("//div[starts-with(@id, 'oglas_')]/div[3]/div[1]/p[1]")

for posao in ids:
    pozicija = posao.text
    linkpozicije = posao.get_attribute(('href'))

    #radi
    #print(posao.text, ", link:", posao.get_attribute('href'))
    pozicija_list = pozicija.split('\n')
    linkpozicije_list = linkpozicije.split('\n')

    dataframe = {'pozicija': pozicija_list, 'link': linkpozicije_list}

    df = pd.DataFrame(dataframe)
    #print(df)

    time.sleep(1)
    df.to_csv('C:/Users/milan/PycharmProjects/job/spisakposlova.csv', mode='a', index=False, header=False)
#, index=False, header=True

    time.sleep(5)

driver.get('https://poslovi.infostud.com/oglasi-za-posao/beograd?education=4&vrste_kategorija_posla=8&working_hours=7&page=2')
items = []
containers = driver.find_elements_by_xpath('//*[@id="__list_jobs"]')
ids = driver.find_elements_by_xpath("//div[starts-with(@id, 'oglas_')]/div[3]/div[1]/h2/a")
#firma = driver.find_element_by_xpath("//div[starts-with(@id, 'oglas_')]/div[3]/div[1]/p[1]")
for posao in ids:
    pozicija = posao.text
    linkpozicije = posao.get_attribute(('href'))
    pozicija_list = pozicija.split('\n')
    linkpozicije_list = linkpozicije.split('\n')
    dataframe = {'pozicija': pozicija_list, 'link': linkpozicije_list}
    df = pd.DataFrame(dataframe)
    time.sleep(1)
    df.to_csv('C:/Users/milan/PycharmProjects/job/spisakposlova.csv', mode='a', index=False, header=False)
    time.sleep(5)

driver.get('https://poslovi.infostud.com/oglasi-za-posao/beograd?education=4&vrste_kategorija_posla=8&working_hours=7&page=3')
items = []
containers = driver.find_elements_by_xpath('//*[@id="__list_jobs"]')
ids = driver.find_elements_by_xpath("//div[starts-with(@id, 'oglas_')]/div[3]/div[1]/h2/a")
#firma = driver.find_element_by_xpath("//div[starts-with(@id, 'oglas_')]/div[3]/div[1]/p[1]")
for posao in ids:
    pozicija = posao.text
    linkpozicije = posao.get_attribute(('href'))
    pozicija_list = pozicija.split('\n')
    linkpozicije_list = linkpozicije.split('\n')
    dataframe = {'pozicija': pozicija_list, 'link': linkpozicije_list}
    df = pd.DataFrame(dataframe)
    time.sleep(1)
    df.to_csv('C:/Users/milan/PycharmProjects/job/spisakposlova.csv', mode='a', index=False, header=False)
    time.sleep(5)

driver.get('https://poslovi.infostud.com/oglasi-za-posao/beograd?education=4&vrste_kategorija_posla=8&working_hours=7&page=4')
items = []
containers = driver.find_elements_by_xpath('//*[@id="__list_jobs"]')
ids = driver.find_elements_by_xpath("//div[starts-with(@id, 'oglas_')]/div[3]/div[1]/h2/a")
#firma = driver.find_element_by_xpath("//div[starts-with(@id, 'oglas_')]/div[3]/div[1]/p[1]")
for posao in ids:
    pozicija = posao.text
    linkpozicije = posao.get_attribute(('href'))
    pozicija_list = pozicija.split('\n')
    linkpozicije_list = linkpozicije.split('\n')
    dataframe = {'pozicija': pozicija_list, 'link': linkpozicije_list}
    df = pd.DataFrame(dataframe)
    time.sleep(1)
    df.to_csv('C:/Users/milan/PycharmProjects/job/spisakposlova.csv', mode='a', index=False, header=False)
    time.sleep(5)

driver.get('https://poslovi.infostud.com/oglasi-za-posao/beograd?education=4&vrste_kategorija_posla=8&working_hours=7&page=5')
items = []
containers = driver.find_elements_by_xpath('//*[@id="__list_jobs"]')
ids = driver.find_elements_by_xpath("//div[starts-with(@id, 'oglas_')]/div[3]/div[1]/h2/a")
#firma = driver.find_element_by_xpath("//div[starts-with(@id, 'oglas_')]/div[3]/div[1]/p[1]")
for posao in ids:
    pozicija = posao.text
    linkpozicije = posao.get_attribute(('href'))
    pozicija_list = pozicija.split('\n')
    linkpozicije_list = linkpozicije.split('\n')
    dataframe = {'pozicija': pozicija_list, 'link': linkpozicije_list}
    df = pd.DataFrame(dataframe)
    time.sleep(1)
    df.to_csv('C:/Users/milan/PycharmProjects/job/spisakposlova.csv', mode='a', index=False, header=False)
    time.sleep(5)


#dodaje link za apliciranje
df = pd.read_csv("spisakposlova.csv")
df["konkurs"] = "https://poslovi.infostud.com/konkurs/"
df.columns = ["Pozicija", "link", "konkurs"]
df['konkurs'] = df['link'].str.extract("(\d\d\d\d\d\d)", expand=True)
df['konkurs'] = 'https://poslovi.infostud.com/konkurs/' + df['konkurs'].astype(str)
df.to_csv("spisakposlova.csv", index=False, header=True)

df = pd.read_csv('spisakposlova.csv')
urls = df['konkurs']

for url in urls:
    data = {}
    driver.get(url)

cv = driver.find_elements_by_xpath('//*[@id="cv_id_293608"]').click();
cover = driver.find_elements_by_xpath('//*[@id="__prijava_pp_text_container"]/div/a').click();
pisi = driver.find_elements_by_xpath('*[@id="tinymce"]').click();