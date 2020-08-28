import pandas as pd
from selenium import webdriver
import time
import csv
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://poslovi.infostud.com/prijava?redirect=%2F')
driver.maximize_window()

#driver.manage().window().maximize();

usernamebox = driver.find_element_by_id("Email_login")
usernamebox.send_keys('milan.krcadinac@gmail.com')

passbox = driver.find_element_by_id("Password_login")
passbox.send_keys('pass')

loginbutton = driver.find_element_by_xpath('//*[@id="Password_login"]')
loginbutton.submit()


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
    driver.find_element_by_id('cv_id_293608').click();
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 1080)")
    time.sleep(2)
    #driver.find_elements_by_xpath('//*[@id="__allow_ct_container"]/div/div/a').click();
    #time.sleep(3)
    driver.find_element_by_id('pp_id_64176').click();
    time.sleep(5)
    driver.find_element_by_id('__prijava-submit').click();
    time.sleep(5)
    driver.find_element_by_id('__prijava-preview-submit').click()
    data.close()
print(url)





#link.csv below
# https://google.com
# https://google.com
# https://google.com



# f = open('spisakposlova.csv', 'r', encoding='utf-8')
# reader = csv.reader(f)
# w = open('output.csv', 'w', newline="", encoding="utf-8")
# writer = csv.writer(w)
#
# for line in reader:
#     driver.get(line[0])
#     time.sleep(5)
#     elements = driver.find_element_by_xpath('//img[@alt="Google"]')
#     writer.writerow(
#              ["Reads", "Average Time Spent", "Impressions", "Read Time", "Likes", "Publication Shares", "Times Stacked",
#               "Link-Outs"])
#
# f.close()
# w.close()