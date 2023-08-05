from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterUserView, EmailVerificationView, ActivationSuccess, \
    ActivationFailed, gen_new_pass, ProfileView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('verify/<str:uidb64>/<str:token>/', EmailVerificationView.as_view(), name='email_verification'),
    path('success', ActivationSuccess.as_view(), name='verify_yes'),
    path('failed', ActivationFailed.as_view(), name='verify_no'),
    path('gen_new_pass/', gen_new_pass, name='gen_new_pass'),
    path('profile/', ProfileView.as_view(),  name='profile_info')
]
