from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd 
import requests
import time
import pymongo
import json
import numpy as np
from webdriver_manager.chrome import ChromeDriverManager


def init_browser():
    #splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    #mars news titles
    browser = init_browser()
    mars_collection = {}

    #Database Setup
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    mars_collection["news_title"] = soup.find('div', class_="content_title").get_text()
    mars_collection["news_snip"] = soup.find('div', class_="rollover_description_inner").get_text()

    #mars images
    url_feature_image = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    browser.visit(url_feature_image)
    response = browser.html
    soup2 = BeautifulSoup(response, 'html.parser')
    images = soup2.find_all('a', class_="fancybox")
    pic_source = []

    for image in images:
        picture = image['data-fancybox-href']
        pic_source.apped(picture)


    mars_collection["featured_image_url"] = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/image/featured/mars2.jpg' 

    #print(mars_collection)
    return mars_collection

#scrape()

