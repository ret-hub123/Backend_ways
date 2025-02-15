import requests
from bs4 import BeautifulSoup

reviewurl = 'https://otzovik.com/review_14063262.html'
response = requests.get(reviewurl)
soup = BeautifulSoup(response.text, 'html.parser')

# 1. Поиск информации об авторе отзыва
author_element = soup.find('a', class_='user-name')
author = author_element.text.strip() if author_element else 'Неизвестно'

# 2. Поиск рейтинга
rating_element = soup.find('span', class_='stars-num')
rating = rating_element.text.strip() if rating_element else 'Нет рейтинга'

# 3. Поиск просмотров
views_element = soup.find('span', class_='review-views')
views = views_element.text.strip() if views_element else 'Нет просмотров'

review_data = {
    'author': author,
    'rating': rating,
    'views': views
}

print(review_data)


from selenium import webdriver

driver = webdriver.Chrome('path/to/chromedriver')

driver.get("https://www.google.com/search?q=good+game")

html = driver.page_source

soup_data = soup(html, "html.parser")
items = soup_data.find("div", {"class": "g"})
items = items.find_all('h3')
titles = []
links = []

for item in items:
    titles.append(item.a.text)
    links.append(item.a['href'])

for i in range(len(titles)):
    print("Title: ", titles[i])
    print("Link: ", links[i])