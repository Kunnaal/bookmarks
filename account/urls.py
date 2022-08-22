from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

# Name of the app
# app_name = 'account'

# Url patterns
urlpatterns = [
    # post views
    # path('login/', views.user_login, name='login'),
    path('', views.dashboard, name='dashboard'),

    # Authorization
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Password change
    # path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # Resetting password
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # Django provided authentication url
    path('', include('django.contrib.auth.urls')),

    # User register path
    path('register/', views.register, name='register'),

    # Path to edit profile
    path('edit/', views.edit, name='edit'),

    # Managing user views
    path('users/', views.user_list, name='user_list'),
    path('users/follow/', views.user_follow, name='user_follow'),
    path('users/<username>/', views.user_detail, name='user_detail'),
]
