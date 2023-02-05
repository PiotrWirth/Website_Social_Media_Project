from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('login/',views.user_login,name='accounts/login'),
    path('logout/',auth_view.LogoutView.as_view(template_name='accounts/logout.html'),name='logout'),
    path('',views.index,name='index'),
    path('password_change/',auth_view.PasswordChangeView.as_view(template_name='accounts/password_change_form.html'),name='password_change'),
    path('password_change/done/',auth_view.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),name='password_change_done'),
    path('password_reset',auth_view.PasswordResetView.as_view(template_name='accounts/password_reset_form.html'),name='password_reset'),
    path('password_reset/done',auth_view.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>',auth_view.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/done',auth_view.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),name='password_reset_complete'),
    path('register/', views.register,name='accounts/register'),
    path('edit/',views.edit,name='accounts/edit'),
]
