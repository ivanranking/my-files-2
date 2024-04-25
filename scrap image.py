import requests
from bs4 import BeautifulSoup as BSP

def split_url(url):
    return url.split('&')[0]

def get_image_urls(search_query):
    url = f"https://cn.bing.com/images/search?q={search_query}&first=1&cw=1177&ch=678"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    rss = requests.get(url, headers=headers)
    soup = BSP(rss.content, "html.parser")

    all_img = []
    for img in soup.find_all('img'):
        img_url = img.get('src2')
        if img_url and img_url.startswith('https://tse2.mm.bing.net/'):
            img_url = split_url(img_url)
            all_img.append(img_url)

    return all_img

print(get_image_urls("cat"))
