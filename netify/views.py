from django.shortcuts import render,redirect,HttpResponse
from .requests import getMovies,trailer_id,movie_details,imdb,get_similar_movies,get_movie_reviews
from .series import getSeries,series_trailer_id,series_details,get_series_reviews
from .search import searchMovies,searchSeries
from .models import Reviews,Company,Season,Series,Movies

# search_url

movie_search_url='https://api.themoviedb.org/3/search/{}?api_key={}&query={}'
movie_search = 'movie'
tv_search = 'tv'

def search(request):
  if 'search_term' in request.GET and request.GET["search_term"]:
    search_name = request.GET.get('search_term')
    found_movies = searchMovies(movie_search_url,movie_search,search_name)
    found_series = searchSeries(movie_search_url,tv_search,search_name)

    context = {
      'found_movies':found_movies,
      'found_series':found_series,
      'search_name':search_name
    }

    return render(request,'search.html',context)
  else:
    return redirect(index)



def index(request):
  context = {

  }

  return render(request,'index.html',context)


# MOVIES



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



# SERIES

# url

series_url='https://api.themoviedb.org/3/tv/{}?api_key={}'

series_details_url='https://api.themoviedb.org/3/tv/{}?api_key={}'

series_tube_id='https://api.themoviedb.org/3/tv/{}/videos?api_key={}'

series_review_url='https://api.themoviedb.org/3/tv/{}/reviews?api_key={}'

series_similar_url='https://api.themoviedb.org/3/tv/{}/similar?api_key={}'

# Searies view function

def series(request):
  
  top_rated_series = getSeries(series_url,'top_rated')
  now_playing_series = getSeries(series_url,'on_the_air')
  upcoming_series = getSeries(series_url,'airing_today')
  popular_series = getSeries(series_url,'popular')

  context = {
    "top_rated_series":top_rated_series,
    "now_playing_series":now_playing_series,
    "upcoming_series":upcoming_series,
    "popular_series":popular_series,
  }

  return render(request,'series.html',context)



# Trailer
def series_tube(request,movie_id):

  series_id_details = series_details(series_details_url,movie_id)
  youtube_video_series_id = series_trailer_id(series_tube_id,movie_id)
  series_reviews = get_series_reviews(series_review_url,movie_id)
  similar_movies = getSeries(series_similar_url,movie_id)

  all_genres = []
  production_companies_name = []
  creators = []
  aired_seasons = []

  try:
    genre = series_id_details['genres']

    for g in genre:
      name = g.get('name')
      all_genres.append(name)

  except:
    all_genres = None

  try:
    companies = series_id_details['production_companies']

    for c in companies:
      name = c.get('name')
      logo = c.get('logo_path')
      origin = c.get('origin_country')
      company_object = Company(name = name, logo = logo, origin = origin)
      production_companies_name.append(company_object)

  except:
    production_companies_name = None


  try:
    created_by = series_id_details['created_by']

    for creator in created_by:
      name = creator.get('name')
      creators.append(name)
  except:
    creators = None


  try:
    seasons = series_id_details['seasons']


    for season in seasons:
      air_date = season.get('air_date')
      episode_count = season.get('episode_count')
      name = season.get('name')
      poster_path = season.get('poster_path')
      season_number = season.get('season_number')

      season_obj = Season(air_date,episode_count,name,poster_path,season_number)

      aired_seasons.append(season_obj)
  except:
    aired_seasons = None


  context = {
    'series_id_details':series_id_details,
    'youtube_video_series_id':youtube_video_series_id,
    'all_genres':all_genres,
    'production_companies_name':production_companies_name,
    # 'countries':countries,
    'similar_movies':similar_movies,
    'series_reviews':series_reviews,
    'creators':creators,
    'aired_seasons':aired_seasons,
  }

  return render(request,'series_play.html',context)

