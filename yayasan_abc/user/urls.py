from django.urls import path
from .views import Users

urlpatterns = [
    # api urls
    path('api/v1/user/', Users.as_view(), name='get_user'),
]