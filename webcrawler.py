from nameparser import HumanName as hn
from bs4 import BeautifulSoup
import requests


def get_video(url):
    print(url)
    try:
        getpage = requests.get(url)
        soup = BeautifulSoup(getpage.text, 'html.parser')
        video_title = soup.find('meta', property="og:title").get("content")
        video_author = soup.find('link', itemprop="name").get("content")
        video_channel = soup.find('span').find('link').get('href')
        video_img = soup.find('meta', property="og:image").get("content")
        video_url = soup.find(rel="shortlinkUrl").get('href')
        video_category = 'Video'
        video_dl = None

        data = (video_title, video_author, video_img, video_url, video_category, video_channel, video_dl)
        return data
    except:
        pass


def get_book(url):
    print(url)
    try:
        getpage = requests.get(url)

        soup = BeautifulSoup(getpage.text, 'html.parser')
        book_dl = soup.find('a', rel="noopener noreferrer nofollow").get('href')
        book_img = soup.find('img', referrerpolicy="no-referrer").get('src')
        book_author = str(hn(soup.find(itemprop="author").string.strip()))
        book_title = soup.find(itemprop="name").string.strip()
        book_category = 'Book'

        data = (book_title, book_author, book_img, url, book_category, None, book_dl)
        return data
    except:
        pass