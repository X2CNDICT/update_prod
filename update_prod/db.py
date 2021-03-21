from pymongo import MongoClient
from urllib.parse import quote_plus


class DB:
  
  def __init__(self, lang, config):
    user = config["user"]
    password = config["password"]
    host = config["host"]
    authdb = config["authdb"]
    uri = "mongodb://{}:{}@{}/{}".format(quote_plus(user), quote_plus(password), host, authdb)
    self.client = MongoClient(uri)
    self.db = self.client["prod_"+lang+"2cn"]

  def insert_into_base(self, vocabs):
    # self.db.base.insert(vocabs)
    pass

  def insert_into_vocabs(self, vocabs):
    # self.db.vocabs.insert(vocabs)
    pass

  def insert_into_extension(self, extensions):
    # self.db.x_extension.insert(extensions)
    pass
