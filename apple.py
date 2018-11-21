""" Our Python user test """
from pymongo import MongoClient

# class Database_klass:
#
def find_user_count():
    print("hello from many users")
    client = MongoClient(port=27017)
    db = client.pybook_test
    result = db.users.find().count()
    print(result)
    return result

    # for i in result:
    #     print (i)
#
# # find()
def find_one_user(user_to_find):
    print("hello from user")
    client = MongoClient(port=27017)
    db = client.pybook_test
    result = db.users.find_one({'user_name': user_to_find})
    print("In find one user")
    print(result)
    # res = None if result == None else result["user_name"]
    # return res
    return None if result == None else result["user_name"]
    #result == None ? return(None) : return(result["user_name"])
#
# def find_user_names():
#     client = MongoClient(port=27017)
#     db = client.pybook_test
#     result = db.users.find()
#     for i in result:
#         print (i["user_name"])
#
def insert_one_user():
    client = MongoClient(port=27017)
    db = client.pybook_test
    load_data = {'user_name': 'winston wolf', 'email': 'w.wolf@pf.com', 'user_message': 'Go to direct line'}
    result = db.users.insert_one(load_data)
    print("inserted!!!")


def delete_one_user(user_to_delete):
    client = MongoClient(port=27017)
    db = client.pybook_test
    load_data = {'user_name': 'winston wolf'}
    result = db.users.delete_many(load_data)
    print("deleted!!!")
    #
# def insert_many_user():
#     client = MongoClient(port=27017)
#     db = client.pybook_test
#     load_data = [{'user_name': 'jules', 'email': 'jules@pf.com', 'user_message': "I'm the foot masuer"},
#     {'user_name': 'mia wallace', 'email': 'mia.wallace@pf.com', 'user_message': 'I like dancing!'}]
#     result = db.users.insert_many(load_data)
#     print(result)
#
# find_one_user()
# print('')
# find_user_names()
# print('')
# insert_many_user()
# print('')
# insert_one_user()
# print('')
# # print (dir(result))
# # for i in result:
# #     print (i)
#
# #
# # result = db.users.find()
# # for i in result:
# #     print (i)
#
# # print (type(result))
#
# # db.users.insert({ user_name: "scarface", email: "al.pacino@makers.com", user_mes
# # sage: "you want to play games"}
#
#
# # load_data = [{'user_name': 'vinca vega', 'email': 'v.vega@pf.com', 'user_message': 'Can i try your $5 shake?'},
# # {'user_name': 'mia wallace', 'email': 'mia.wallace@pf.com', 'user_message': 'I like dancing!'}]
# # result = db.users.insert_many(load_data)
# #
# # result = db.users.find()
# # for i in result:
# #     print (i)
