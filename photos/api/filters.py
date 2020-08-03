import django_filters
from photos.models import Photo
from django.contrib.auth.models import User

class PhotoFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(method='filter_user')
    photo_type = django_filters.CharFilter(method='filter_photo_type')

    class Meta:
        model = Photo
        fields = ['publisher','status']

    def filter_user(self, queryset, name, value):
        filtered_set = queryset.filter(publisher__username=value)
        return filtered_set

    def filter_photo_type(self, queryset, name, value):
        user = self.request.user

        if value == 'my_photos':
            return queryset.filter(publisher=user)
        elif value == 'my_drafts':
            return queryset.filter(publisher=user, status='draft')

        return queryset

        