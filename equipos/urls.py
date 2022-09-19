from django.urls import path
from equipos import views

app_name = "equ"


urlpatterns = [
    path("teams_list/", views.TeamsList.as_view(), name="teams_list"),
    path("teams_detail/<int:pk>/", views.TeamsDetail.as_view(), name="teams_detail"),
    path("create_team/", views.CreateTeams.as_view(), name="create_team"),
    path("teams_update/", views.TeamsUpdate.as_view(), name="teams_update"),
    path("index", views.index.as_view(), name="index"),
    path('delete_team/<int:pk>/', views.TeamsDelete, name="delete_team"),
]