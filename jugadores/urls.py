from django.urls import path
from jugadores import views

app_name = "jug"


urlpatterns = [
    path("players_list/", views.PlayersList.as_view(), name="players_list"),
    path("player_detail/<int:pk>/", views.PlayersDetail.as_view(), name="player_detail"),
    path("create_player/", views.CreatePlayer.as_view(), name="create_player"),
    path("player_update/", views.PlayersUpdate.as_view(), name="player_update"),
    path("index", views.index.as_view(), name="index"),
    path('player_delete/<int:pk>/', views.PlayerDelete, name="player_delete"),
]