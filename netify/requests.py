import requests
from decouple import config
import json
import re
from .models import Movies,Reviews


# The movies url

# Get movie by category url

movie_url ='https://api.themoviedb.org/3/movie/{}?api_key={}'

# Get movie youtube video id

movie_trailer='https://api.themoviedb.org/3/movie/{}/videos?api_key={}'

# Get a movies details

movie_details_url='https://api.themoviedb.org/3/movie/{}?api_key={}'

# imdb (internet movie database):

imdb_url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

# Get similar movie to the searched one

similar_movies_url='https://api.themoviedb.org/3/movie/{}/similar?api_key={}'

# Get movie reviews

movie_review_url='https://api.themoviedb.org/3/movie/{}/reviews?api_key={}'

# The youtube url

# plays the video id

youtube='https://www.googleapis.com/youtube/v3/search?part=snippet&q={}&key={}'

# The API keys

api_key = config('MOVIE_API_KEY')
key = config('YOUTUBE_API_KEY')
    
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
    if poster_path != None:
      movie_object = Movies(popularity,vote_count,poster_path,id,original_language,original_title,vote_average,overview,release_date)
      list.append(movie_object)
    else:
      continue
    
  return list

# function that get the first trailer id
def trailer_id(movie_id):

  trailers_url = movie_trailer.format(int(movie_id),api_key)
  response = requests.get(trailers_url)
  data = response.json()
  the_id = data['results'][0].get('key')

  return the_id

# function that gets a specific movies details
def movie_details(movie_id):

  details_url = movie_details_url.format(movie_id,api_key)
  response = requests.get(details_url)
  data = response.json()

  return data

# function that contacts imdb
# Not really necessary...info is almost simmilar as that from novie database
# Usefull if added info is required

def imdb(imdb_id):

  querystring = {"i":imdb_id,"r":"json"}

  headers = {
      'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
      'x-rapidapi-key': config('x-rapidapi-key')
      }

  response = requests.request("GET", imdb_url, headers=headers, params=querystring)

  return response

# search similar movies
def get_similar_movies(movie_id):
  complete_url = similar_movies_url.format(movie_id,api_key)
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
    if poster_path != None:
      movie_object = Movies(popularity,vote_count,poster_path,id,original_language,original_title,vote_average,overview,release_date)
      list.append(movie_object)
    else:
      continue

  return list
  
def get_movie_reviews(movie_id):
  complete_url = movie_review_url.format(movie_id,api_key)
  response = requests.get(complete_url)
  data = response.json()

  reviews = []
  for review in data['results']:
    author = review.get('author')
    content = review.get('content')
    url = review.get('url')
    if content != None and author != None:
      new_review = Reviews(author = author, content = content, url = url)
      reviews.append(new_review)
    else:
      continue

  return reviews