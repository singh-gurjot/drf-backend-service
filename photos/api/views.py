from photos.models import Photo
from photos.api.serializers import PhotoSerializer
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django_filters import rest_framework as filters
from photos.api.filters import PhotoFilter
from drf_backend_service import settings
import os


class PhotoList(generics.ListCreateAPIView):
    parser_classes = (MultiPartParser,FormParser,JSONParser)
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
            image_key = image_url.split('/')[1]
            file_path = os.path.join(settings.ASSET_ROOT, image_key)
            print (file_path)
            if os.path.isfile(file_path):
                os.remove(file_path)
        
        instance.delete()
