from django.conf.urls import url

from slackvideoapp import views
app_name = 'polls'
urlpatterns = [
    url('home/', views.home, name='index'), # url for home page
    url('jukebox/', views.jukebox, name='jukebox'), #url for video listing page
]
