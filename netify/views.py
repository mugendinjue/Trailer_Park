from django.shortcuts import render
from .requests import getMovies
import json
import requests
from decouple import config
import re
import random



hobs = 'https://www.youtube.com/watch?v=HZ7PAyCDwEg'
youtube='https://www.googleapis.com/youtube/v3/search?part=snippet&q={}&key={}'

def home(request):
  popular_movies = getMovies('popular')
  top_rated_movies = getMovies('upcoming')
  now_playing = getMovies('now_playing')
  
 
  random_movies = []
  for movies in popular_movies:
    random_movies.append(movies)
  for top in top_rated_movies:
    random_movies.append(top)
  for playing in now_playing:
    random_movies.append(playing)
  list_length = len(random_movies)

  display1 = random.randint(0,list_length-1)
  movie1 = random_movies[display1]
  display2 = random.randint(0,list_length-1)
  movie2 = random_movies[display2]
  display3 = random.randint(0,list_length-1)
  movie3 = random_movies[display3]
  context = {
    "movie":popular_movies,
    "top_movies":top_rated_movies,
    "now_playing":now_playing,
    "first_movie":movie1,
    "first_movie":movie1,
    "second_movie":movie2,
    "third_movie":movies
  }

  return render(request,'home.html',context)



# class Spliter:
#   def __init__(self):
#     pass
#   def id_from_url(self,url:str):
#     return url.rsplit("=",1)[1]
#   def clean_title(self,title):
#     title = re.sub('[\W_:,]',"_",title)
#     return title.lower()


# spliter = Spliter()
# print(spliter.id_from_url(hobs))



# key = config('YOUTUBE_API_KEY')
# video_id = "C0PuCgQrxZU"
# url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}"

# data = requests.get(url)
# jason_data = data.json()
# print(jason_data)

