from flask import Flask, request, render_template
from flask_pymongo import PyMongo
app = Flask(__name__)

### connecting to mongodb database ###
try: 
    app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
    mongo = PyMongo(app)
    print("Successfully connected to the database :)")
except: 
    print("Something went wrong :(")


### routing ###
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/find",  methods=["GET"])
def home_page():
    online_users = mongo.db.flightsData.find({"age": 68})
    return render_template("index.html",
        online_users=online_users)


if __name__ == "__main__":
    app.run(port=80, debug=True)