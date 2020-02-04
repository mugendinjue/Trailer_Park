import requests
from decouple import config
import json
from .models import Reviews,Series


# keys

api_key = config('MOVIE_API_KEY')
key = config('YOUTUBE_API_KEY')

# function that gets the series

def getSeries(url,category):
  complete_url = url.format(category,api_key)
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


# function that get the first trailer id
def series_trailer_id(url,movie_id):

  trailers_url = url.format(int(movie_id),api_key)
  response = requests.get(trailers_url)
  data = response.json()
  the_id = data['results'][0].get('key')

  return the_id

# function that gets a specific series details
def series_details(url,movie_id):

  details_url = url.format(movie_id,api_key)
  response = requests.get(details_url)
  data = response.json()

  return data

def get_series_reviews(url,movie_id):
  complete_url = url.format(movie_id,api_key)
  response = requests.get(complete_url)
  data = response.json()

  reviews = []
  for review in data['results']:
    author = review.get('author')
    content = review.get('content')
    url = review.get('url')

    new_review = Reviews(author = author, content = content, url = url)
    reviews.append(new_review)

  return reviews