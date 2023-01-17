from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  
driver = webdriver.Chrome("C:\D\python\Bots\crypto\selenuim\chromedriver.exe")

def get_coin_price(coin_name):
    coins_data={
    }
    driver.get(f"https://coinmarketcap.com/currencies/{coin_name}/markets/")
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(5)
    x=0
    while x < 5:
        try:
            driver.find_elements(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div/div[7]/button')[0].click()
            time.sleep(3)
            x+=1
        except IndexError:
            break
    time.sleep(3)
    # driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div[2]/div[4]/div/table/thead/tr/th[1]/div/div/span/span').click()

    # coin_index=driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div/div[4]/div/table/tbody/tr[1]/td[1]/p').get_attribute("innerHTML")

    for x in range(0, 400):
        try:
            exchanger = driver.find_elements(By.XPATH, f'//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div/div[4]/div/table/tbody/tr[{x}]/td[2]/span/a[1]/div/div/p')
            pair=driver.find_elements(By.XPATH, f'//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div/div[4]/div/table/tbody/tr[{x}]/td[3]/div/a')
            price=driver.find_elements(By.XPATH, f'//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div/div[4]/div/table/tbody/tr[{x}]/td[4]/p')

            if len(exchanger) == 1:
                # print(exchanger[0].get_attribute("innerHTML"))
                print(pair[0].get_attribute("innerHTML"))
                # print(price[0].get_attribute("innerHTML"))  
                if pair[0].get_attribute("innerHTML") in coins_data:
                    coins_data[pair[0].get_attribute("innerHTML")][exchanger[0].get_attribute("innerHTML")]=price[0].get_attribute("innerHTML") 
                else:
                    coins_data[pair[0].get_attribute("innerHTML")]={
                            exchanger[0].get_attribute("innerHTML"):price[0].get_attribute("innerHTML")           
                    }
        except :
            break
    print(coins_data)

    for coin in coins_data.keys():
        highest_value=0
        lowest_value=100000000000000000000000000000000000000000000000000000000000000
        for exchanger in coins_data[coin].keys():
            price=float(coins_data[coin][exchanger].replace("$", "").replace("*", "").replace(" ", "").replace(",", ""))
            if price > highest_value:
                highest_value=price
                highest_exchanger=exchanger
            if price < lowest_value:
                lowest_value=price
                lowest_exchanger=exchanger
        
        

        price_diff=highest_value-lowest_value
        profit=(price_diff/highest_value)*100
        if profit > 10:
            print(f"Highest Price {coin} {highest_exchanger} {highest_value}")
            print(f"Lowest Price {coin} {lowest_exchanger} {lowest_value}")
            print(f"Profit: {profit}")
            print("..................................................................")
            print("\n\n\n")


get_coin_price('dogecoin')


    

