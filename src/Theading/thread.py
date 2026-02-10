import threading
import requests
from bs4 import BeautifulSoup

urls = [
    f"https://www.cnblogs.com/#p{page}"
    for page in range(1, 10)
]

def craw(url):
    r = requests.get(url)
    return r.text

def multi_thread():
    threads = []
    for url in urls:
        threads.append(
            threading.Thread(target=craw, args=(url,))
        )

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

def parse(html):
    # class="post-item-title" 每页数据的标题类名
    soup = BeautifulSoup(html, "html.parser") # html.parser 是 Python 的标准库 BeautifulSoup 中的一个解析器，用于解析 HTML 和 XML 文档。
    links = soup.find_all('a', class_="post-item-title")
    return [(link["href"], link.get_text()) for link in links]
    


if __name__ == '__main__':
    for result in parse(craw(urls[0])):
        print(result)