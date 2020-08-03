from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('api/v1/', views.SnippetList.as_view()),
    path('api/v1/<int:pk>/', views.SnippetDetail.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = format_suffix_patterns(urlpatterns)


