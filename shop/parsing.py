import requests
from bs4 import BeautifulSoup


url = 'https://habr.com/ru/news/'
r = requests.get(url).text
soup = BeautifulSoup(r, "html.parser")

# first news


def habr_link1():
    link = soup.find_all('a', class_='post__title_link')[0].get('href')
    return link


def habr_img1():
    try:
        img = soup.find_all('div', class_='post__text post__text-html js-mediator-article')[0]
        image = img.find('img').get('src')
        return image
    except:
        return '<img src="/static/images/nopic.png"/>'


def habr_text1():
    text = soup.find_all('a', class_='post__title_link')[0].text
    return text

# second news


def habr_link2():
    link = soup.find_all('a', class_='post__title_link')[1].get('href')
    return link


def habr_img2():
    try:
        img = soup.find_all('div', class_='post__text post__text-html js-mediator-article')[1]
        image = img.find('img').get('src')
        return image
    except:
        return '<img src="/static/images/nopic.png"/>'


def habr_text2():
    text = soup.find_all('a', class_='post__title_link')[1].text
    return text


# third news

def habr_link3():
    link = soup.find_all('a', class_='post__title_link')[2].get('href')
    return link


def habr_img3():
    try:
        img = soup.find_all('div', class_='post__text post__text-html js-mediator-article')[2]
        image = img.find('img').get('src')
        return image
    except:
        return '<img src="/static/images/nopic.png"/>'


def habr_text3():
    text = soup.find_all('a', class_='post__title_link')[2].text
    return text