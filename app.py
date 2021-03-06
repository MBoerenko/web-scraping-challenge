  
from flask import Flask, render_template, redirect, request
from flask_pymongo import PyMongo
import scrape_mars
import time


app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    destination_data = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", mars_data=destination_data)

# Route that will trigger the scrape function
@app.route("/scrape")
def browser_init():

    mars_data=scrape_mars.browser_init()

    # Run the scrape function

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_data, upsert=True)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)