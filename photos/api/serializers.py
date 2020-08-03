from rest_framework import serializers
from photos.models import Photo

class PhotoSerializer(serializers.ModelSerializer):
    publisher = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Photo
        fields = '__all__'