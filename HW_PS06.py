from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd


options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)


driver.get("https://www.divan.ru/category/divany-i-kresla")
time.sleep(5)  # Даем странице загрузиться

products = []


cards = driver.find_elements(By.CSS_SELECTOR, 'div._Ud0k')
for card in cards:
    try:
        name = card.find_element(By.CSS_SELECTOR, 'div.lsooF span').text
        price = card.find_element(By.CSS_SELECTOR, 'div.pY3d2 span').text
        link = card.find_element(By.TAG_NAME, 'a').get_attribute('href')

        products.append({
            'Название': name,
            'Цена': price,
            'Ссылка': link
        })
    except Exception as e:
        print(f"Ошибка при парсинге карточки: {e}")

driver.quit()


df = pd.DataFrame(products)
df.to_csv('divan_data.csv', index=False, encoding='utf-8-sig')
print("Данные успешно сохранены в divan_data.csv")