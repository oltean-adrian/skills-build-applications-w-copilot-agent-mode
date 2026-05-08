from pymongo import MongoClient
from django.conf import settings

def get_db():
    client = MongoClient(host='localhost', port=27017)
    return client[settings.DATABASES['default']['NAME']]
