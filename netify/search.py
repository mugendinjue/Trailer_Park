import requests
from decouple import config
import json
from .models import Reviews,Series,Movies


# keys

api_key = config('MOVIE_API_KEY')
key = config('YOUTUBE_API_KEY')

def searchMovies(url,search_type,search_name):
  complete_url = url.format(search_type,api_key,search_name)
  response = requests.get(complete_url)
  movies = response.json()

  list = []
  for new_movie in movies["results"]:
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

def searchSeries(url,search_type,search_name):
  complete_url = url.format(search_type,api_key,search_name)
  response = requests.get(complete_url)
  movies = response.json()
  

  list = []
  for new_movie in movies['results']:
    popularity = new_movie.get('popularity')
    vote_count = new_movie.get('vote_count')
    poster_path = new_movie.get('poster_path')
    id = new_movie.get('id')
    original_language = new_movie.get('original_language')
    original_name = new_movie.get('original_name')
    vote_average = new_movie.get('vote_average')
    overview = new_movie.get('overview')
    release_date = new_movie.get('release_date')
    if poster_path != None:
      movie_object = Series(popularity,vote_count,poster_path,id,original_language,original_name,vote_average,overview,release_date)
      list.append(movie_object)
    else:
      continue
  return list