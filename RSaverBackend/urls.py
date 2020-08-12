

from django.urls import path, include
from . import views
from rest_framework import routers


# router=routers.DefaultRouter()
# router.register(r'user',AuthUserAPIView)

urlpatterns=[
    # path('',include(router.urls)),
    # login for browsable api
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    path('auth_user',views.auth_user,name='authenticate_user'),
    path('add_user',views.add_user,name='add_new_user'),
    # path('user/',AuthUserAPIView.as_view(),name='user_endpoint'),
] 