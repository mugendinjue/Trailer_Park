from django.urls import path,re_path
from . import views


urlpatterns = [

  path('',views.index,name='index'),
  re_path(r'^movies/$',views.home,name='home'),
  re_path(r'^movie_trailer/(?P<movie_id>\d+)$',views.tube,name='movie'),
  re_path(r'^series/$',views.series, name='series'),
  re_path(r'^series_trailer/(?P<movie_id>\d+)$',views.series_tube, name='series_tube'),
  re_path(r'^search/item/$',views.search,name='search'),
]
