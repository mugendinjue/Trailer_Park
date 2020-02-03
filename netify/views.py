from django.shortcuts import render
from .requests import getMovies,trailer_id

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
  
  youtube_video_id = trailer_id(movie_id)
  context = {
    'youtube_video_id':youtube_video_id,
  }

  return render(request,'test.html',context)
