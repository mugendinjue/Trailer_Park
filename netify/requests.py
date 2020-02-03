import requests
from decouple import config
import json
import re

# The movie url

movie_url ='https://api.themoviedb.org/3/movie/{}?api_key={}'

# The youtube url
youtube='https://www.googleapis.com/youtube/v3/search?part=snippet&q={}&key={}' 

# The API keys

api_key = config('MOVIE_API_KEY')
key = config('YOUTUBE_API_KEY')

# A class that splits and clean the urls to search

class Spliter:
  def __init__(self):
    pass
  def id_from_url(self,url:str):
    return url.rsplit("=",1)[1]
  def clean_title(self,title):
    title = re.sub('[\W_:,]',"_",title)
    return title.lower()

# calls the splitter class

hah = Spliter()


# The movie blueprint

class Movies():
  def __init__(self,popularity,vote_count,poster_path,id,original_language,original_title,vote_average,overview,release_date):
    self.popularity = popularity
    self.vote_count = vote_count
    self.poster_path = 'https://image.tmdb.org/t/p/w500/'+poster_path
    self.id = id
    self.original_language = original_language
    self.original_title = original_title
    self.vote_average = vote_average
    self.overview = overview
    self.release_date = release_date
  
    
# The function that sends the request to movie database api

def getMovies(category):
  complete_url = movie_url.format(category,api_key)
  response = requests.get(complete_url)
  movies = response.json()
  

  list = []
  for new_movie in movies['results']:
    popularity = new_movie.get('popularity')
    vote_count = new_movie.get('vote_count')
    poster_path = new_movie.get('poster_path')
    id = new_movie.get('id')
    original_language = new_movie.get('original_language')
    original_title = new_movie.get('original_title')
    vote_average = new_movie.get('vote_average')
    overview = new_movie.get('overview')
    release_date = new_movie.get('release_date')

    movie_object = Movies(popularity,vote_count,poster_path,id,original_language,original_title,vote_average,overview,release_date)
    list.append(movie_object)
  return list