
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def price_bitcoin(hostname):
    try :
        # Deixar navegador oculto
        #options = webdriver.ChromeOptions()
        #options.add_argument("--headless")
        
        # Abre o navegado com configurações acima
        driver = webdriver.Chrome()#chrome_options=options)
        driver.get(hostname)  

        # Efetua busca no Google
        bar = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
        bar.send_keys('bitcoin')
        time.sleep(1)

        # Clica no botão Pesquisar
        search = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]")
        search.click()
        time.sleep(1)

        # Pega o preço do Bitcoin 
        bitcoin = driver.find_element_by_xpath('/html/body/div[7]/div/div[10]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[2]')
        pricebtc =(f"Preço Bitcoin hoje: {bitcoin.text}")
        
        return(pricebtc, 1)

    except:
        return('ERRO BTC', 0)


