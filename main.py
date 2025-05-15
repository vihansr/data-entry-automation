from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup

url = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

prices = soup.select(".PropertyCardWrapper__StyledPriceLine")
addresses = soup.select("a.StyledPropertyCardDataArea-anchor")

all_prices = [price.get_text().strip().replace("mo", "").replace("/","").replace("1bd","").replace("1 bd", "") for price in prices]
all_addresses = [add.get_text().strip() for add in addresses]
all_links = [link['href'] for link in addresses]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdPOKPTak6OeJfI3e3nihWDyZHRuBDmKwfgIfAJxEfDUOObUQ/viewform")
time.sleep(2)

for n in range(len(all_links)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdPOKPTak6OeJfI3e3nihWDyZHRuBDmKwfgIfAJxEfDUOObUQ/viewform")
    time.sleep(2)

    address = driver.find_element(by=By.XPATH,
                                  value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')
    price = driver.find_element(by=By.XPATH,
                                value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(by=By.XPATH,
                               value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
    submit_button = driver.find_element(by=By.XPATH,
                                        value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')

    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    submit_button.click()