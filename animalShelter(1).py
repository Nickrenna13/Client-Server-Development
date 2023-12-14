#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 15:32:54 2023

@author: nicholasrenna_snhu
"""
 
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        #USER = 'aacuser'
        #PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30177 #30177
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
        #print statement for connection success
        print ("Connection Successful")

# Create method to implement the CREATE in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary
            return True            
        else:
            raise Exception("Nothing to create, because data parameter is empty")
            return False

# Read method to implement the READ in CRUD.
    def read(self, data):
        try:
            
            if data is not None:
                readResult = list(self.database.animals.find(data, {"_id":0})) # data should be dictionary and returns the result
                return readResult
            else:
                return []
        #For Exception handling during READ operations in CRUD
        except Exception as e:
            print("A error has occured. Check read data or read search parameters:", e)
            
# Update method to implement the UPDATE in CRUD
    def update(self, data, newData):
        try:
            if data is not None:
                updatedResult = self.database.animals.update_many(data, {"$set": newData}) # data should be a dictionary
                return updatedResult.modified_count # returns the updated result with the modified count for verification
            else:
                return []
        
        # Exception handling for the update method
        except Exception as e:
                print("A error has occured. Check update format:", e)
       
# Delete Method to Implement the DELETE in CRUD
    def delete(self, data):
        try:
            if data is not None:
                deleteResult = self.database.animals.delete_one(data) # data should be a dictionary
                return deleteResult.deleted_count # returns the count of the deleted document
            else:
                return [] # if deleted then empty brackets will display 
            
        # Exception handling for the delete method in CRUD
        except Exception as e:
            print("An error has occured. Check delete parameters: ", e)
                
        
            
            