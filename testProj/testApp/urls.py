from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('playlists/', views.playlists, name='playlists'),
    path('episodes/', views.episodes, name='episodes'),
    path('submit_story/', views.submit_story, name='submit_story'),
    path('voicenote/', views.voicenote, name='voicenote'),
    path('colors/', views.colors, name='colors'),
    path('voicenote/success', views.vn_success, name='vn_success'),
]