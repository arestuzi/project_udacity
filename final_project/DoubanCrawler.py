#!/usr/bin/env python
# coding=utf-8
import expanddouban
import csv
import os
import time
from bs4 import BeautifulSoup
from collections import OrderedDict

base_url = 'https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影'

class Movie:
    """
    Unused
    """
    def __init__(self, name, rate, location, category, info_link, cover_link):
        self.name = name
        self.rate = rate
        self.location = location
        self.category = category
        self.info_link = info_link
        self.cover_link = cover_link

def getMovieUrl(category, location):
    """
    Return a string corresponding to the URL of douban movie lists given category and location.
    """
    url = base_url + ','+ category + ',' + location
    return url

def getMovies(category, location):
    """
    Capture and format the information of movies
    """
    movies = []
    locations = checkLocation(category,location)

    for location in locations:
        url = getMovieUrl(category, location)
        html = expanddouban.getHtml(url, loadmore = True)
        soup = BeautifulSoup(html, 'html.parser')
        for obj in soup.find('div', class_="list-wp").find_all('a', target="_blank"):
            object = []
            object.append(obj.p.find('span', class_="title").get_text())
            object.append(obj.p.find('span', class_="rate").get_text())
            object.append(location)
            object.append(category)
            object.append(obj.get('href'))
            object.append(obj.find('span', class_="pic").find('img').get('src'))
            movies.append(object)

    return movies

def writeCsvFile(fname, data):
    """
    Write and append if the file exists.
    """
    if not os.path.isfile(fname):
        csvfile = open(fname, 'w', encoding='utf-8', newline='')
        writer = csv.writer(csvfile)
        writer.writerows(data)
        csvfile.close()
    else:
        csvfile = open(fname, 'a', encoding='utf-8', newline='')
        writer = csv.writer(csvfile)
        writer.writerows(data)
        csvfile.close()



def checkLocation(category,location):
    """
    Update location for each movie.
    """
    url = getMovieUrl(category,location)
    html = expanddouban.getHtml(url, loadmore = False)
    soup = BeautifulSoup(html, 'html.parser')
    if location == '全部地区':
        locations = []
        for location in soup.find_all('ul', class_='category'):
            if location.find('span', class_='tag-checked').get_text() == '全部地区':
                for location in location.find_all('span', class_='tag'):
                    locations.append(location.get_text())
                locations.remove('全部地区')
                return locations
    else:
        return location

def topThree(fname, categories):
    """
    Find out the TOP 3 movies for each category
    """
    with open(fname, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        movies = list(reader)

    f = open('output.txt', 'w', encoding='utf-8')
    total_movies = {}
    for category in categories:
        locations = {}

        for movie in movies:
            if category not in total_movies and movie[3] == category:
                total_movies[category] = 1
            elif category in total_movies and movie[3] == category:
                total_movies[category] += 1
            if movie[2] not in locations and movie[3] == category:
                locations[movie[2]] = 1
            elif movie[2] in locations and movie[3] == category:
                locations[movie[2]] += 1
        locations_sorted_by_value = sorted(locations.items(), key=lambda x: x[1], reverse=True)
        print("电影类别: %s" % category, file=f)
        print("数量排名前三的地区及占总数的百分比: ", end=" ",file=f)
        for i in range(3):
            result  = "%.2f" % (locations_sorted_by_value[i][1] / total_movies[category] * 100 )
            print(locations_sorted_by_value[i][0] + str(result) + "%", end=" ", file=f)
        print("", file=f)
    f.close()

fname = 'movies.csv'
categories = ["恐怖", "剧情", "战争"]
location = '全部地区'
if os.path.isfile(fname):
    try:
        os.remove(fname)
    except:
        print("This should not display")

for category in categories:
    movies = getMovies(category, location)
    writeCsvFile(fname, movies)

topThree(fname, categories)



