from rest_framework import serializers
from photos.models import Photo
from django.contrib.auth.models import User
class PhotoSerializer(serializers.ModelSerializer):
    publisher_name = serializers.ReadOnlyField(source='publisher.username')

    class Meta:
        model = Photo
        read_only_fields = ('publisher_name',)
        fields = ('id', 'status', 'title', 'caption', 'image', 'created_at', 'publisher_name', 'published_at')