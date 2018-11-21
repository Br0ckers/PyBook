""" Our Python user test """
from pymongo import MongoClient
# from randon import randint
client = MongoClient(port=27017)
# print(client)
db=client.pybook_test
# print(db)

# result = db.users.find_one({'user_name': "joe bloggs"})
# print(result)

# result = db.users.find()
# for i in result:
#     print (i)

# result = db.users.find()
# for i in result:
#     print (i["user_name"])

# load_data = {'user_name': 'vinca vega', 'email': 'v.vega@pf.com', 'user_message': 'Can i try your $5 shake?'}
# result = db.users.insert_one(load_data)
#
# print (dir(result))
# for i in result:
#     print (i)

#
# result = db.users.find()
# for i in result:
#     print (i)

# print (type(result))

# db.users.insert({ user_name: "scarface", email: "al.pacino@makers.com", user_mes
# sage: "you want to play games"}


load_data = [{'user_name': 'vinca vega', 'email': 'v.vega@pf.com', 'user_message': 'Can i try your $5 shake?'},
{'user_name': 'mia wallace', 'email': 'mia.wallace@pf.com', 'user_message': 'I like dancing!'}]
result = db.users.insert_many(load_data)

result = db.users.find()
for i in result:
    print (i)
