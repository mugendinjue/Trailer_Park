from django.shortcuts import render
from .requests import getMovies,trailer_id,movie_details,imdb,get_similar_movies,get_movie_reviews



# companies object

class Company:
  def __init__(self,name,logo,origin):
    self.name = name
    self.logo = logo
    self.origin = origin

# The home view function with movie posters

def home(request):
  top_rated_movies = getMovies('top_rated')
  now_playing_movies = getMovies('now_playing')
  upcoming_movies = getMovies('upcoming')
  popular_movies = getMovies('popular')

  context = {
    "top_rated_movies":top_rated_movies,
    "now_playing_movies":now_playing_movies,
    "upcoming_movies":upcoming_movies,
    "popular_movies":popular_movies,
  }

  return render(request,'home.html',context)

#  view function with youtube video player

def tube(request,movie_id):
  
  try:
    the_movie_details = movie_details(movie_id)
  except:
    the_movie_details = 'Service not available at the moment'

  try:
    youtube_video_id = trailer_id(movie_id)
  except:
    youtube_video_id = 'Service not available at the moment'

  try:
    similar_movies = get_similar_movies(movie_id)
  except:
    similar_movies = 'Service not available at the moment'

  try:
    movie_reviews = get_movie_reviews(movie_id)
  except:
    movie_reviews = 'Service not available at the moment'

  all_genres = []
  production_countries = []
  production_companies_name = []

  genre = the_movie_details['genres']
  countries = the_movie_details['production_countries']
  companies = the_movie_details['production_companies']
  
  for g in genre:
    name = g.get('name')
    all_genres.append(name)

  for p in countries:
    name = p.get('name')
    production_countries.append(name)

  for c in companies:
    name = c.get('name')
    logo = c.get('logo_path')
    origin = c.get('origin_country')
    company_object = Company(name = name, logo = logo, origin = origin)
    production_companies_name.append(company_object)
  print(movie_reviews)
  context = {

    'youtube_video_id':youtube_video_id,
    'the_movie_details':the_movie_details,
    'all_genres':all_genres,
    'production_countries':production_countries,
    'production_companies_name':production_companies_name,
    'similar_movies':similar_movies,
    'movie_reviews':movie_reviews,
  }

  return render(request,'test.html',context)
