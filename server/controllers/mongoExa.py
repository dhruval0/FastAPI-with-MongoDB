import pymongo

def add_query(name, email, age, languages, password):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["application"]
    mycol = mydb["users"]

    user_info = {
        "name" : f"{name}",
        "email" : f"{email}",
        "age" : f"{age}",
        "languages" : f"{languages}",
        "password" : f"{password}"
    }
    
    x = mycol.insert_one(user_info)
    
    return {"message" : "Succesfully created your account"}
    # x = mycol.insert_one(mydict)
    # y = mycol.insert_one(mydict2)

    # for one in mycol.find():
    #     print(one.get("_id"))

    myquery = ({"name" : {"$regex" : "^a"}})
    x = mycol.delete_many(myquery)
