from django.urls import path
from textToBraille.views import TranslationViewSet

index = TranslationViewSet.as_view({'get': 'list', 'post': 'create'})
index_file = TranslationViewSet.as_view({'get': 'list', 'post': 'convert_file'})
detail = TranslationViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'})

urlpatterns = [
    path('text', index, name='text-list'),
    path('text/<str:pk>', detail, name='text-detail'),
    path('file', index_file, name='file-list'),
]