from django.contrib import admin
from django.urls import path

from playlists import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("tracks/", views.TrackListView.as_view(), name="track-list"),
]
