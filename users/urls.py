from .views import *
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name="auth-login"),
    path('auth/logout/', LogoutView.as_view(), name="auth-logout"),
    path('register/verify/code=<str:token>/',SetPasswordAndActivate,name="email-activator"),
    path('register/',RegistrationView.as_view(),name="registration"),
    path('resetpassemail/',ResetPasswordEmail,name="resetpass-email"),
    path('resetpass/code=<str:token>/',ResetPassword,name="resetpass"),
    path('follow/', FollowUserView.as_view(), name="follow-user"),
    path('unfollow/', UnfollowUserView.as_view(), name="follow-user"),
    path('feed/', UserFeedView.as_view(), name='fetch-feed'),
    path('<int:pk>/posts/', PostsByUserView.as_view(), name="posts-by-user"),
    path('bookmarks/',PostsByBookmarksView.as_view(),name="posts_by_bookmarks"),
    path('profile/',UserView.as_view(),name="view-logged-in-user")
]
