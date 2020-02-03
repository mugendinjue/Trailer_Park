from django.urls import path,re_path
from . import views


urlpatterns = [

  path('',views.home,name='home'),
  re_path(r'^movie_trailer/(?P<movie_id>\d+)$',views.tube,name='movie'),

]
