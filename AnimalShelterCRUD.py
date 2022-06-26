from pymongo import MongoClient
from bson.objectid import ObjectId
import json

#create a class for the AAC shelter
class AnimalShelter(object):

#label as the CRUD ops for definition and easy recall
    """Animals Collection in MongoDB CRUD Ops"""

    #define and init self with authentication
    def __init__(self, username, password):
        #init the MongoClient for DB access with necessary credentials and auth source due to issues
        self.client = MongoClient('mongodb://%s:%s@localhost:54259' % (username, password))
        #init database with client
        self.database = self.client['AAC']

    #TEDDIE- CCCCreate method to implement the C in CRUD
    def create(self, data=dict()):
        #verify if data is empty
        if data is not None:
            #checking search results for return -  data should be dictionary
            self.database.animals.insert_one(data) 
        else: 
            raise Exception("Nothing to create because data parameter is empty")


    #TEDDIE- RRRRead data in animals table to implement the R in CRUD
    def read(self, data):
    #Verify that search criteria was provided, else raise an exception
        if data is not None:
            #TEDDIE - adjust to find instead of insert to read
            return self.database.animals.find(data,{"_id":False})
        else:
            raise Exception("Nothing to create because data parameter is empty")
    
    
    #TEDDIE- UUUUpdate method time for the U in CRUD
    def update(self, find=dict(), replace=dict()):
        #TEDDIE- if not none
        if fine is not None:
            #TEDDIE- dict should be the data
            x= self.database.aniamls.update_many(find, {"$set":replace})
            return json.dumps(str(x.modified_count) + 'updates have occured')
        else:
            raise Exception("Nothing to update because the data parameter is empty")
            
     #TEDDIE- DDDDeleting information for the D in CRUD
    def delete(self, data=dict()):
        if data is not None:
            return json.dumps(self.database.animals.remove(data), indent = 4)
        else:
            raise Exception("Nothing to delete because the data parameter is empty")
