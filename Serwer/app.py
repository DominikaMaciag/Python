from flask import Flask, Response
import pymongo
app = Flask(__name__)

### connecting to mongodb database ###
try: 
    mongo = pymongo.MongoClient(host="localhost", port=27017, serverSelcetionTimeoutMS = 1000)
    db = mongo.user_DB #tworzymy bazkę user_DB
    mongo.server_info()
    #print("Successfully connected to the database :)")
except: 
    print("Something went wrong :(")


### routing ###
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/users", methods=["POST"])
def createUser():
    try:
        user = {'name': "Jan Kowalski", 'age': 45}
        dbResponse = db.users.insert_one(user) #wrzucamy do kolekcji 'users'
        print(dbResponse.inserted_id)
        return Response(
            response={"message": "user created", "id":f"{dbResponse.inserted_id}"},
            status = 200,
            mimetype = "application/json"
        )
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    app.run(port=80, debug=True)