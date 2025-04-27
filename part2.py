import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Запуск драйвера
driver = webdriver.Chrome()

url = "https://samara.hh.ru/vacancies/programmist"
driver.get(url)
time.sleep(5)

# Ищем все карточки вакансий
vacancies = driver.find_elements(By.CLASS_NAME, "vacancy-card--n77Dj8TY8VIUF0yM")  # изменено на правильный класс

parsed_data = []

for vacancy in vacancies:
    try:
        title = vacancy.find_element(By.CSS_SELECTOR, "[data-qa='serp-item__title']").text
        link = vacancy.find_element(By.CSS_SELECTOR, "[data-qa='serp-item__title']").get_attribute("href")

        try:
            company = vacancy.find_element(By.CSS_SELECTOR, "[data-qa='vacancy-serp__vacancy-employer-text']").text
        except:
            company = "Компания не указана"

        try:
            salary_element = vacancy.find_element(By.CSS_SELECTOR, "span.magritte-text_typography-label-1-regular___pi3R-_3-0-32")
            salary = salary_element.text.replace('\u00A0', ' ').replace('\u202F', ' ').strip()
            if not salary:
                salary = "Зарплата не указана"
        except:
            salary = "Зарплата не указана"

        parsed_data.append([title, company, salary, link])

    except Exception as e:
        print(f"Ошибка парсинга: {e}")
        continue

driver.quit()

# Запись в CSV файл
with open("vacancies.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Название вакансии", "Компания", "Зарплата", "Ссылка"])
    writer.writerows(parsed_data)

print("Данные успешно записаны в файл vacancies.csv")
