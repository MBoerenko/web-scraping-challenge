from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup
import pandas as pd
import pymongo
#import lxml.html as lh
#import urllib.request
#from urllib.request import urlopen
import re

def init_browser():
    #Windows Users / Open Chromedriver
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

# NASA MARS NEWS

    # Mars news URL of page to be scraped
    news_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_url)

    #Create beautifulsoup object
    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')

    # Retrieve the latest news title and paragraph
    news_title = news_soup.find_all('div', class_='content_title')[1].text
    news_description = news_soup.find_all('div', class_='article_teaser_body')[0].text

    print(news_title)
    print("======================================")
    print(news_description)

    #JPL MARS SPACE IMAGES - FEATURED IMAGE
    #Define URL
    base_url = 'https://www.jpl.nasa.gov'
    images_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    browser.visit(images_url)

    #Create beautiful soup object
    image_html = browser.html
    image_soup = BeautifulSoup(image_html, 'html.parser')

    #scrape article and carousel item from website
    finddiv = image_soup.find('article', class_="carousel_item")

    #locate html for url
    style_text = finddiv["style"]
    print(style_text)

    #truncate style_text to include only the url
    style_text.find("('")
    style_text.find("')")
    image_url=style_text[21+len("('"):75]
    print (image_url)

    #Put the base url and image url together
    featured_url = base_url + image_url
    featured_url

    # MARS FACTS

    dfs=pd.read_html('https://space-facts.com/mars/')
    dfs[0].columns=['Description', 'Value']
    dfs[0]

    mars_html = dfs[0].to_html()
    print(mars_html)

    # MARS HEMISPHERES

    hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemisphere_url)

    hemisphere_html = browser.html
    hemisphere_soup = BeautifulSoup(hemisphere_html, 'html.parser')

    hemisphere_image_urls = []

    titles = hemisphere_soup.find_all('h3')

    for i in range(len(titles)):
        title = titles[i].text
        print(title)
        
        hemis_images = browser.find_by_tag('h3')
        hemis_images[i].click()
        
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        
        img_url = soup.find('img', class_='wide-image')['src']
        img_url = "https://astrogeology.usgs.gov" + img_url
        print(img_url)
        
        hemis_dict = {"title": title, "img_url":img_url}
        hemisphere_image_urls.append(hemis_dict)
        
    hemisphere_image_urls


    # Store data in a dictionary
    mars_data= {
        "news_title": news_title,
        "news_description": news_description,
        "featured_url": featured_url,
        "mars_facts": dfs,
        "hemisphere_images": hemisphere_image_urls
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data

