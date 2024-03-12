import pymongo

# MongoDB connection details
# Add your connection details here

# Connect to the MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["phone_book"]

# Access the collections
contacts_col = db["contacts"]
addresses_col = db["addresses"]
phone_numbers_col = db["phone_numbers"]
contact_phone_col = db["contact_phone"]
contact_address_col = db["contact_address"]

# Delete all documents in the collections
contacts_col.delete_many({})
addresses_col.delete_many({})
phone_numbers_col.delete_many({})
contact_phone_col.delete_many({})
contact_address_col.delete_many()

print("All previous data has been deleted.")
