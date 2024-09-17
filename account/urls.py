from django.urls import path, include

from .views import SignUp, SignIn, logout_user, UserProfile

urlpatterns = [
    path("/signup", SignUp, name="signup"),
    path("/login", SignIn, name="signin"),
    path("/profile", UserProfile, name="profile"),
    path("/logout", logout_user, name="logout"),
]
