from django.urls import path

from .views import HomeView, Users


urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    # api urls
    path('api/v1/user/', Users.as_view(), name='get_user'),
]
