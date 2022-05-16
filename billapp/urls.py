from django.urls import path, include
from . import views
from accounts import views as acc_views
from django.contrib.auth import views as a_views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', acc_views.RegistrationView.as_view(), name='register'),
    path('login/', acc_views.LoginView.as_view(), name='login'),
    path('logout/', acc_views.logout, name='logout'),
    path('activate/<uidb64>/<token>', acc_views.VerificationView.as_view(), name='activate'),
    path('reset_password/', acc_views.PasswordResetView.as_view(template_name='password_reset.html'), name='reset_password'),
    path('reset_password_sent/', a_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', a_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete/', a_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'), name='password_reset_complete'),
    path('<slug>/edit/', acc_views.update_profile, name='update'),
    path('<slug>/', acc_views.ShowProfile.as_view(), name='show_profile'),
    path('apps/', include('apps.urls')),
    
]