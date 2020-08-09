

from django.urls import path
from .views import AuthUserAPIView

urlpatterns=[
    path('user/',AuthUserAPIView.as_view(),name='user_endpoint'),
] 