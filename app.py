from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Function that connects our web app and the code that powers it
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

# Function that connects the web scraping route
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   print("SCRAPING... SCRAPING... SCRAPING")
   mars_data = scraping.scrape_all()
   print("HERE I AM... HERE I AM... HERE I AM")
   mars.update_one({}, {"$set":mars_data}, upsert=True)
   return redirect('/', code=302)

# Run it
if __name__ == "__main__":
   app.run()   