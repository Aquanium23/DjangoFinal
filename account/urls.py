from django.urls import path
from .views import UserRegistrationView, UserLoginView, user_logout, user_account_activation, UserProfileView, \
    UserProfileUpdateView

urlpatterns = [
    path("user-profile-update/", UserProfileUpdateView.as_view(), name="user_profile_update"),
    path("user-profile/", UserProfileView.as_view(), name="user_profile"),
    path("activate/<str:username>/<str:activation_key>/", user_account_activation, name="user_account_activation"),
    path("user-logout/", user_logout, name="user_logout"),
    path("user-login/", UserLoginView.as_view(), name="user_login"),
    path("register/", UserRegistrationView.as_view(), name="user_register")
]
