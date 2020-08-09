

from django.urls import path
from .views import AuthUserView

urlpatterns=[
    path('user/',AuthUserAPIView.as_view(),name='user_endpoint'),
] 