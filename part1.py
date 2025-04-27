import requests
from bs4 import BeautifulSoup

url = "https://"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
rows = soup.find_all("td")
data = []

for raw in rows:
    cols = raw.find_all("td")
    cleaned_cols = [col.text.strip() for col in cols]
    data.append(cleaned_cols)

print(data)
