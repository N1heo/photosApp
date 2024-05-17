from rest_framework import generics

from photo_edit.models import Photo_edit
from . import serializers
from user.models import User
from photos.models import Image
from album.models import Album, AlbumImage

class ListCreateUsersView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class RetrieveUpdateDestroyUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class ListCreateImagesView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = serializers.ImageSerializer

class RetrieveUpdateDestroyImageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = serializers.ImageSerializer

class ListCreateAlbumsView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = serializers.AlbumSerializer

class RetrieveUpdateDestroyAlbumView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = serializers.AlbumSerializer

class ListCreateAlbumImagesView(generics.ListCreateAPIView):
    queryset = AlbumImage.objects.all()
    serializer_class = serializers.AlbumImageSerializer

class RetrieveUpdateDestroyAlbumImageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AlbumImage.objects.all()
    serializer_class = serializers.AlbumImageSerializer

class ListCreatePhotoEditView(generics.ListCreateAPIView):
    queryset = Photo_edit.objects.all()
    serializer_class = serializers.PhotoEdit
