from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from django.conf.urls.static import static
from drf_backend_service import settings

urlpatterns = [
    path('api/v1/', views.SnippetList.as_view()),
    path('api/v1/<int:pk>/', views.SnippetDetail.as_view())
]

urlpatterns += static(settings.ASSET_URL, document_root=settings.ASSET_ROOT)
urlpatterns = format_suffix_patterns(urlpatterns)


