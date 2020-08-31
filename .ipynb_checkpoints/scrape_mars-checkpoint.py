{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from splinter import Browser\n",
    "from splinter.exceptions import ElementDoesNotExist\n",
    "from bs4 import BeautifulSoup\n",
    "import pandas as pd\n",
    "import lxml.html as lh\n",
    "import urllib.request\n",
    "from urllib.request import urlopen\n",
    "import re"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Windows Users / Open Chromedriver\n",
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "NASA MARS NEWS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Define URL\n",
    "url = 'https://mars.nasa.gov/news/'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Mars news URL of page to be scraped\n",
    "news_url = 'https://mars.nasa.gov/news/'\n",
    "browser.visit(news_url)\n",
    "\n",
    "#Create beautifulsoup object\n",
    "html = browser.html\n",
    "news_soup = BeautifulSoup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "NASA Engineers Checking InSight's Weather Sensors\n",
      "======================================\n",
      "An electronics issue is suspected to be preventing the sensors from sharing their data about Mars weather with the spacecraft.\n"
     ]
    }
   ],
   "source": [
    "# Retrieve the latest news title and paragraph\n",
    "news_title = news_soup.find_all('div', class_='content_title')[1].text\n",
    "news_p = news_soup.find_all('div', class_='article_teaser_body')[0].text\n",
    "\n",
    "print(news_title)\n",
    "print(\"======================================\")\n",
    "print(news_p)"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "JPL MARS SPACE IMAGES - FEATURED IMAGE"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Define URL\n",
    "base_url = 'https://www.jpl.nasa.gov'\n",
    "images_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "\n",
    "browser.visit(images_url)\n",
    "\n",
    "#Create beautiful soup object\n",
    "image_html = browser.html\n",
    "image_soup = BeautifulSoup(image_html, 'html.parser')\n",
    "\n",
    "#scrape article and carousel item from website\n",
    "finddiv = image_soup.find('article', class_=\"carousel_item\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "background-image: url('/spaceimages/images/wallpaper/PIA00063-1920x1200.jpg');\n"
     ]
    }
   ],
   "source": [
    "#locate html for url\n",
    "style_text = finddiv[\"style\"]\n",
    "print(style_text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "/spaceimages/images/wallpaper/PIA00063-1920x1200.jpg\n"
     ]
    }
   ],
   "source": [
    "#truncate style_text to include only the url\n",
    "style_text.find(\"('\")\n",
    "style_text.find(\"')\")\n",
    "image_url=style_text[21+len(\"('\"):75]\n",
    "print (image_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://www.jpl.nasa.gov/spaceimages/images/wallpaper/PIA00063-1920x1200.jpg'"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Put the base url and image url together\n",
    "featured_url = base_url + image_url\n",
    "featured_url"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "MARS FACTS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Description</th>\n",
       "      <th>Value</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Equatorial Diameter:</td>\n",
       "      <td>6,792 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Polar Diameter:</td>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Moons:</td>\n",
       "      <td>2 (Phobos &amp; Deimos)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Orbit Distance:</td>\n",
       "      <td>227,943,824 km (1.38 AU)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Orbit Period:</td>\n",
       "      <td>687 days (1.9 years)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Surface Temperature:</td>\n",
       "      <td>-87 to -5 °C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>First Record:</td>\n",
       "      <td>2nd millennium BC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Recorded By:</td>\n",
       "      <td>Egyptian astronomers</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            Description                          Value\n",
       "0  Equatorial Diameter:                       6,792 km\n",
       "1       Polar Diameter:                       6,752 km\n",
       "2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       "3                Moons:            2 (Phobos & Deimos)\n",
       "4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       "5         Orbit Period:           687 days (1.9 years)\n",
       "6  Surface Temperature:                   -87 to -5 °C\n",
       "7         First Record:              2nd millennium BC\n",
       "8          Recorded By:           Egyptian astronomers"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dfs=pd.read_html('https://space-facts.com/mars/')\n",
    "dfs[0].columns=['Description', 'Value']\n",
    "dfs[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<table border=\"1\" class=\"dataframe\">\n",
      "  <thead>\n",
      "    <tr style=\"text-align: right;\">\n",
      "      <th></th>\n",
      "      <th>Description</th>\n",
      "      <th>Value</th>\n",
      "    </tr>\n",
      "  </thead>\n",
      "  <tbody>\n",
      "    <tr>\n",
      "      <th>0</th>\n",
      "      <td>Equatorial Diameter:</td>\n",
      "      <td>6,792 km</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>1</th>\n",
      "      <td>Polar Diameter:</td>\n",
      "      <td>6,752 km</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>2</th>\n",
      "      <td>Mass:</td>\n",
      "      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>3</th>\n",
      "      <td>Moons:</td>\n",
      "      <td>2 (Phobos &amp; Deimos)</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>4</th>\n",
      "      <td>Orbit Distance:</td>\n",
      "      <td>227,943,824 km (1.38 AU)</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>5</th>\n",
      "      <td>Orbit Period:</td>\n",
      "      <td>687 days (1.9 years)</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>6</th>\n",
      "      <td>Surface Temperature:</td>\n",
      "      <td>-87 to -5 °C</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>7</th>\n",
      "      <td>First Record:</td>\n",
      "      <td>2nd millennium BC</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>8</th>\n",
      "      <td>Recorded By:</td>\n",
      "      <td>Egyptian astronomers</td>\n",
      "    </tr>\n",
      "  </tbody>\n",
      "</table>\n"
     ]
    }
   ],
   "source": [
    "mars_html = dfs[0].to_html()\n",
    "print(mars_html)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "MARS HEMISPHERES"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Cerberus Hemisphere Enhanced\n",
      "https://astrogeology.usgs.gov/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg\n",
      "Schiaparelli Hemisphere Enhanced\n",
      "https://astrogeology.usgs.gov/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg\n",
      "Syrtis Major Hemisphere Enhanced\n",
      "https://astrogeology.usgs.gov/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg\n",
      "Valles Marineris Hemisphere Enhanced\n",
      "https://astrogeology.usgs.gov/cache/images/5277a23c6d8a3a325985965390cb77a2_valles_marineris_unenhanced.tif_full.jpg\n"
     ]
    }
   ],
   "source": [
    "hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "browser.visit(hemisphere_url)\n",
    "\n",
    "html = browser.html\n",
    "hemisphere_soup = BeautifulSoup(html, 'html.parser')\n",
    "\n",
    "hemisphere_image_urls = []\n",
    "\n",
    "titles = hemisphere_soup.find_all('h3')\n",
    "\n",
    "for i in range(len(titles)):\n",
    "    title = titles[i].text\n",
    "    print(title)\n",
    "    \n",
    "    hemis_images = browser.find_by_tag('h3')\n",
    "    hemis_images[i].click()\n",
    "    \n",
    "    html = browser.html\n",
    "    soup = BeautifulSoup(html, 'html.parser')\n",
    "    \n",
    "    img_url = soup.find('img', class_='wide-image')['src']\n",
    "    img_url = \"https://astrogeology.usgs.gov\" + img_url\n",
    "    print(img_url)\n",
    "    \n",
    "    hemis_dict = {\"title\": title, \"img_url\":img_url}\n",
    "    hemisphere_image_urls.append(hemis_dict)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'title': 'Cerberus Hemisphere Enhanced',\n",
       "  'img_url': 'https://astrogeology.usgs.gov/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg'},\n",
       " {'title': 'Schiaparelli Hemisphere Enhanced',\n",
       "  'img_url': 'https://astrogeology.usgs.gov/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg'},\n",
       " {'title': 'Syrtis Major Hemisphere Enhanced',\n",
       "  'img_url': 'https://astrogeology.usgs.gov/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg'},\n",
       " {'title': 'Valles Marineris Hemisphere Enhanced',\n",
       "  'img_url': 'https://astrogeology.usgs.gov/cache/images/5277a23c6d8a3a325985965390cb77a2_valles_marineris_unenhanced.tif_full.jpg'}]"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hemisphere_image_urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
