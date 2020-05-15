from django.conf.urls import url
from . import views

urlpatterns=[
    url('',views.welcome,name = 'welcome'),
    url('',views.news_of_day,name='newsToday'),
    #to allow users to input days on urls to get news.
    url('archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews'),
    ] 
