from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from photos.api import views
from django.conf.urls.static import static
from drf_backend_service import settings

urlpatterns = [
    path('v1/photos/', views.PhotoList.as_view()),
    path('/v1/photos/<int:pk>/', views.PhotoDetail.as_view())
]

urlpatterns += static(settings.ASSET_URL, document_root=settings.ASSET_ROOT)
urlpatterns = format_suffix_patterns(urlpatterns)


