from django.urls import path

from .views import SSOLoginView, SSOLogoutView, UserInfo

urlpatterns = [
    # authentication
    path('login/', SSOLoginView.as_view(), name='token_login'),
    path('logout/', SSOLogoutView.as_view(), name='token_logout'),
    path('info/', UserInfo.as_view(), name='user_info'),
]
