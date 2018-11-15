# import necessary libraries
from flask import Flask, render_template, session, redirect
from scrape_mars import scrape
from bs4 import BeautifulSoup
from splinter import Browser
import requests
import lxml
import time
import sys
import json


# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo

# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)
#print(client, file=sys.stderr)

# Connect to a database. Will create one if not already available.
db = client['marshw_db']

collection=db['mars']
#print(collection, file=sys.stderr)

collection.drop()
#collection.insert_one({"objecz":42})

# # create route that renders index.html template
@app.route("/")
def index():
    marsdict = dict(collection.find_one())
    print(marsdict, file=sys.stderr)
    return render_template("index.html", marsdict=marsdict)


@app.route("/scrape")
def mongosetup():
    with open('scrape.json') as f:
        scraperesults = json.load(f)
    collection = db['mars']
    # # this runs the actual scraper, or you can just use the recent scrape results from the JSON file
    # scraperesults = scrape()
    collection.insert_one(scraperesults)
    return redirect("http://localhost:5000/")

if __name__ == "__main__":
    app.run(debug=True)