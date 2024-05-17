from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path("users/", views.ListCreateUsersView.as_view(), name="list-create-users"),
    path("user/<int:pk>/", views.RetrieveUpdateDestroyUserView.as_view(), name="retrieve-update-destroy-user"),
    path("images/", views.ListCreateImagesView.as_view(), name="list-create-images"),
    path("image/<int:pk>/", views.RetrieveUpdateDestroyImageView.as_view(), name="retrieve-update-destroy-image"),
    path("albums/", views.ListCreateAlbumsView.as_view(), name="list-create-albums"),
    path("album/<int:pk>/", views.RetrieveUpdateDestroyAlbumView.as_view(), name="retrieve-update-destroy-album"),
    path("album-images/", views.ListCreateAlbumImagesView.as_view(), name="list-create-album-images"),
    path("album-image/<int:pk>/", views.RetrieveUpdateDestroyAlbumImageView.as_view(), name="retrieve-update-destroy-album-image"),
    path("photo_edit/", views.ListCreatePhotoEditView.as_view(), name="list-create-photo-edit")]
