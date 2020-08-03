from photos.models import Photo
from myapi.serializers import PhotoSerializer
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django_filters import rest_framework as filters
from api.filters import PhotoFilter
from drf_backend_service import settings
import os


class PhotoList(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ("publisher", "status",)
    filterset_class = PhotoFilter
    ordering_fields = ['created_at']


    def perform_create(self, serializer):
        serializer.save(publisher=self.request.user)


class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def perform_update(self, serializer):
        serializer.save(publisher=self.request.user)

    def perform_destroy(self, instance):
        if instance.image:
            image_url = instance.image.url
            file_path = os.path.join(settings.MEDIA_ROOT,image_url.replace(settings.MEDIA_URL,""))
            
            if os.path.isfile(file_path):
                os.remove(file_path)
        
        instance.delete()
