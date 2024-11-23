from django.urls import path
from .views import HomeView, Users, SSOLoginView, SSOLogoutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    # api urls
    path('api/v1/user/', Users.as_view(), name='get_user'),

    # authentication
    path('auth/login/', SSOLoginView.as_view(), name='token_login'),
    path('auth/logout/', SSOLogoutView.as_view(), name='token_logout'),
]