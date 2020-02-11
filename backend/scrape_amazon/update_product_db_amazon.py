from scrape_objects_MVP import get_attributes
from pymongo import MongoClient

CLIENT = MongoClient("mongodb+srv://XXXXXX:XXXXXXX@cluster0-swsn8.mongodb.net/test?retryWrites=true&w=majority")
DB = CLIENT.compurator
PRODUCTS_COLLECTION = DB["products"]


def add_product_amazon(PRODUCTS_COLLECTION, url):
    '''
    :param PRODUCTS_COLLECTION, url:
    :return prod_document: dictionary containing attributes of product on amazon
    '''

    prod_document = get_attributes(url)

    # product already exists in database
    # remove it in case price has been updated, then re-add. Can optimize by checking whether or not price has changed, but can fix later
    if PRODUCTS_COLLECTION.find({'p_id': prod_document['p_id']}) is not None:
        PRODUCTS_COLLECTION.delete_one({'p_id': prod_document['p_id']})

    PRODUCTS_COLLECTION.insert_one(prod_document)

    return prod_document
