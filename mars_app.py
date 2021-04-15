from flask import Flask, redirect, render_template
from flask_pymongo import PyMongo
import scrape_mars

#create flask
app = Flask(__name__)

#PyMongo to connect to Mongo
app.config["MONGO_URI"]="mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#Flask routes
@app.route("/")
def home(): 
    mars = mongo.db.mars.find_one()
    print(mars)
#Return template     
    #return "homepage"
    return render_template("index.html", mars=mars)

#route to trigger scrape function
@app.route("/scrape")
def scrape():

    #run scrape function
    mars_data = scrape_mars.scrape()

    #update the mongo
    mongo.db.mars.update({}, mars_data, upsert=True)

    #redirect
    return redirect("/")

if __name__ == "__main__":
    app.run(debug = True)