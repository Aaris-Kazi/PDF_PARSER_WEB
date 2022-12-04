# from django.test import TestCase

# Create your tests here.
# a= """
# Resume
# Name: John Doe
# Age: 12
# Gender: Male
# Education : B.E Computer Engg
# """
# # print(a)
# a = a.split('\n')
# text = {}
# for i in a:
#     # print(i)
#     if ":" in i:
#         # print(i)
#         i = i.split(":")
#         text[i[0]] = i[1]
# print(text)
from pymongo import MongoClient
data = {'Name': ' John Doe', 'Age': ' 12', 'Gender': ' Male', 'Education ': ' B.E Computer Engg'}
cluster = MongoClient("localhost:27017")
db = cluster['static_data']
collection = db['resume']
collection.insert_one(data)
result =  collection.find()
print(result)