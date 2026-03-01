
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name="acc"

urlpatterns = [
      path('register/',views.register,name='register'),
      path('password_reset_confirm/<uidb64>/<token>',views.activate,name='activate'),
     
    # LOGINs
    path("login/", views.login_bl, name="login"),

    # LOGOUT
    path("logout/", views.logout_bl, name="logout"),

    # CHANGE PASSWORD
    path("password-change/",
         auth_views.PasswordChangeView.as_view(
             template_name="registrations/emails/cha_pass.html",
             success_url="/"
         ),
         name="password_change"),

    # RESET PASSWORD
    path("password-reset/",
         auth_views.PasswordResetView.as_view(
             template_name="registrations/emails/password_reset_form.html",
             email_template_name="registrations/emails/resetPass_em.html",
             success_url='/reg/password-reset/done/'
         ),
         name="password_reset"),

    path("password-reset/done/",
         auth_views.PasswordResetDoneView.as_view(
             template_name="registrations/emails/password_reset_done.html"
         ),
         name="password_reset_done"),

    path(
    "password_reset_confirm/<uidb64>/<token>/",
    views.CustomPasswordResetConfirmView.as_view(
        template_name="regiistrations/emails/password_reset_confirm.html",
        success_url="/"
    ),
    name="password_reset_confirm",),

    path("profile/", views.profile, name="profile"),
path('profile/edit/', views.edit_profile, name='edit_profile'),
path('profile/delete/', views.delete_account, name='delete_account'),
]


