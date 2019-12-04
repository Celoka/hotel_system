from django.urls import path
from user.views import RegisterUserView, LoginView, ImageUploadView, index

urlpatterns = [
    path('', index, name="home-route"),
    path('auth/register/', RegisterUserView.as_view(), name="auth-register"),
    path('auth/login/', LoginView.as_view(), name="auth-login"),
    path('user/upload/', ImageUploadView.as_view(), name="file-upload"),
    path('user/upload/<int:pk>/', ImageUploadView.as_view(), name="file-upload-detail")
]