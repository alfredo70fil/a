from django.urls import path
from estadios import views

app_name = "est"


urlpatterns = [
    path("stadiums_list/", views.StadiumList.as_view(), name="stadiums_list"),
    path("stadium_detail/<int:pk>/", views.StadiumDetail, name="stadium_detail"),
    path("create_stadium/", views.CreateStadium.as_view(), name="create_stadium"),
    path("stadium_update/<int:pk>/", views.StadiumUpdate.as_view(), name="stadium_update"),
    path("index", views.index.as_view(), name="index"),
    path('delete_stadium/<int:pk>/', views.StadiumsDelete, name="delete_stadium"),
]