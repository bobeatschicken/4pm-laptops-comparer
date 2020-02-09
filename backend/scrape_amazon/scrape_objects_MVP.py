import requests
import string
from bs4 import BeautifulSoup
import re

# user-agent request header
# docs: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# input: product url from amazon
# output: dictionary with item title, price, and id
def get_attributes(url):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'lxml')

    title = get_title(soup)
    price = get_price(soup)
    item_id = get_id(url)

    return {
        'title': title,
        'price': price,
        'id': item_id
    }


# input: object containing HTML that is parsed
# output: product title (up to the first , or ( or | character
def get_title(soup):
    title = soup.find(id="productTitle")

    if title is None:
        return None

    title = str(title.get_text().strip())
    title = re.search(r'.+?(?=[,(|])', title).group(0)
    return title


# input: object containing HTML that is parsed
# output: most probable price (using heuristics)
# NOTE: price will vary! max deviation looked to be ~$100 so far
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


# input: product url on amazon
# output: item id based on either dp or gp
def get_id(url):
    item_id = re.search(r'(\/dp\/|\/gp\/)\w+(\/|$)', url).group(0)
    if item_id[-1] == '/':
        item_id == item_id[:-1]

    return item_id[4:]