from photos.models import Photo
from photos.api.serializers import PhotoSerializer
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.exceptions import PermissionDenied
from django_filters import rest_framework as filters
from photos.api.filters import PhotoFilter
from drf_backend_service import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, ParseError
import json
import os
from datetime import datetime
from django.utils import timezone

class PhotoList(generics.ListCreateAPIView):
    serializer_class = PhotoSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PhotoFilter
    ordering_fields = ['created_at']

    def get_queryset(self):
        queryset = Photo.objects.all()
        user = self.request.user
        photos_type = self.request.query_params.get('photos_type', None)
        username = self.request.query_params.get('username', None)
        if username:
            return queryset.filter(publisher__username=username)

        if photos_type == 'my_photos':
            return queryset.filter(publisher=user)

        elif photos_type == 'my_drafts':
            return queryset.filter(publisher=user, status='draft')

        else:
            return queryset.filter(status='live')
        

    def perform_create(self, serializer):
        serializer.save(publisher=self.request.user)


class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def perform_update(self, serializer):
        instance = self.get_object()
        published_at = None
        print (instance.__dict__)
        print(instance.publisher, self.request.user)

        if instance.publisher != self.request.user:
            raise PermissionDenied()

        if instance.status == 'live':
            published_at = timezone.now()

        serializer.save(publisher=self.request.user, published_at = published_at)

    def perform_destroy(self, instance):
        if instance.publisher != self.request.user:
            raise PermissionDenied()

        if instance.image:
            image_url = instance.image.url
            image_key = image_url.split('/')[1]
            file_path = os.path.join(settings.ASSET_ROOT, image_key)
            print(file_path)
            if os.path.isfile(file_path):
                os.remove(file_path)

        instance.delete()
