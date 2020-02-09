import requests
import string
from bs4 import BeautifulSoup
import re

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def get_attributes(url):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'lxml')

    price = get_price(soup)
    title = get_title(soup)

    return {
        'title': title,
        'price': price,

    }


def get_title(soup):
    title = soup.find(id="productTitle")

    if title is None:
        return None

    title = str(title.get_text().strip())
    title = re.search(r'.+?(?=[,(|])', title).group(0)
    return title


def get_price(soup):
    html_prices = list()

    price = soup.find(class_="priceBlockBuyingPriceString")
    html_prices.append(price)
    deal = soup.find(id="priceblock_dealprice")
    html_prices.append(deal)
    item_id = soup.find(id="priceblock_ourprice")
    html_prices.append(item_id)

    html_prices = list(filter(None, html_prices))

    for idx, html in enumerate(html_prices):
        if len(html) == 0:
            continue
        html_prices[idx] = html.get_text()

    # print(html_prices)

    return max(set(html_prices), key=html_prices.count)



if __name__ == '__main__':
    url = 'https://www.amazon.com/HP-Dual-Core-Processor-Bluetooth-14-cb161wm/dp/B07YXSLFDH/ref=sr_1_3?keywords=hp+laptop&qid=1581187417&s=electronics&sr=1-3'
    print(get_attributes(url))