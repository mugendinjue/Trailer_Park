from django.db import models

# Movie blueprint

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


# Series blueprint
class Series():
  def __init__(self,popularity,vote_count,poster_path,id,original_language,original_name,vote_average,overview,release_date):
    self.popularity = popularity
    self.vote_count = vote_count
    self.poster_path = 'https://image.tmdb.org/t/p/w500/'+poster_path
    self.id = id
    self.original_language = original_language
    self.original_name = original_name
    self.vote_average = vote_average
    self.overview = overview
    self.release_date = release_date



# Reviews blueprint
class Reviews:
  def __init__(self,author,content,url):
    self.author = author
    self.content = content
    self.url = url


# companies object

class Company:
  def __init__(self,name,logo,origin):
    self.name = name
    self.logo = logo
    self.origin = origin

# seasons object

class Season:
  def __init__(self,air_date,episode_count,name,poster_path,season_number):
    self.air_date = air_date
    self.episode_count = episode_count
    self.name = name
    self.poster_path = 'https://image.tmdb.org/t/p/w500/'+poster_path
    self.season_number = season_number