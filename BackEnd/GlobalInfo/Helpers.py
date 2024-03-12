import BackEnd.GlobalInfo.Keys as connectKeys
from pymongo import MongoClient


def dbConnection():
    if connectKeys.dbconn is None:
        mongoConnect = MongoClient(connectKeys.mongoUrl)
        connectKeys.dbconn = mongoConnect['nttDataBlog']
    return connectKeys.dbconn