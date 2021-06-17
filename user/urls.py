from django.urls import path
from django.contrib.auth import views as as_view
from user import views
from .views import PasswordsChangeView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('login/' , as_view.LoginView.as_view(template_name = "login.html") , name= "login"),
    path('logout/' , as_view.LogoutView.as_view() , name= "logout") , 
    path('register/' ,views.register , name="register" ),
    path('profile/<pk>/' , views.profile , name="profile" ),
    path('profile/<pk>/password_change/', PasswordsChangeView.as_view(template_name='password_change.html'), name='PasswordsChangeView'),
    path('profile/<pk>/password_change/done', auth_views.PasswordChangeDoneView.as_view(), name = 'password_change_done'),
    ##### Rest password urls ########
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
]
