from scrape_objects_MVP import get_attributes
import json


def test_price(products_dict):
    for idx, url in enumerate(products_dict):
        print(products_dict[url])
        print(get_attributes(url))
        print('---')

if __name__=='__main__':
    with open('./test_scrape.JSON') as f:
        products_dict = json.load(f)
    test_price(products_dict)
