from scrape_objects_MVP import get_attributes
from pymongo import MongoClient

def setup():
    '''
    set up client for mongo DB and read URL text file

    :return: products_collection, list of lines from text file of URLs
    '''
    client = MongoClient("mongodb+srv://XXXXXX:XXXXXXX@cluster0-swsn8.mongodb.net/test?retryWrites=true&w=majority")
    db = client.compurator
    products_collection = db["products"]

    file_object = open('laptop_urls.txt')
    lines = file_object.readlines()

    return products_collection, lines

def add_product_amazon(products_collection, lines):
    '''
    adds product documents to mongo DB product collection based on list of URLs
    in the text file, URLs above the --- denote unadded products

    :param lines: list of lines from input text file of URLs
    :return: None
    '''

    for line in lines:
        if line == '---':
            break

        url = str(line.strip())
        prod_document = get_attributes(url)

        # product already exists in database
        # remove it in case price has been updated, then re-add. Can optimize by checking whether or not price has changed, but can fix later
        if products_collection.find({'p_id': prod_document['p_id']}) is not None:
            products_collection.delete_one({'p_id': prod_document['p_id']})

        products_collection.insert_one(prod_document)

        # print(url)

if __name__=='__main__':
    products_collection, lines = setup()
    add_product_amazon(products_collection, lines)