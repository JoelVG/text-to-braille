from django.urls import path
from textToBraille.views import TranslationViewSet

index = TranslationViewSet.as_view({'get': 'list', 'post': 'create'})
detail = TranslationViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'})

urlpatterns = [
    path('text', index, name='text-list'),
    path('text/<str:pk>', detail, name='text-detail')
]