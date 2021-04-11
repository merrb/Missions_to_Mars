from flask import Flask
from flask_pymongo import flask_pymongo
import scrape_mars

#create flask
app = Flask(__name__)

#PyMongo to connect to Mongo
mongo = PyMongo(app, url="mongodb://localhost:27017/mars_app")

#Flask routes
@app.route("/")
def home(): 
    mars = mongo.db.mars.find_one()

#Return template     
    #return "homepage"
    return render_template("index.html", mars=mars_info)

#route to trigger scrape function
    @app.route("/scrape")
    def scrape():

    #run scrape function
    mars_data = scrape_mars.scrape()

    #update the mongo
    mongo.db.collection.update({}, mars_data, upsert=True)

    #redirect
    return redirect("/")

if __name__ == "__main__":
    app.run(debug = True)