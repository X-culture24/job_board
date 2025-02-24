from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_view, login_view, logout_view, dashboard, index,profile_form,job_listings,post_list, post_reaction

urlpatterns = [
    path("", index, name="index"),  # Homepage
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("dashboard/", dashboard, name="dashboard"),
    path("profile/", profile_form, name="profile_form"),  # Profile page
    path("jobs/", job_listings, name="job_listings"),  # Job listings page
    path("posts/", post_list, name="post_list"),
    path("posts/<int:post_id>/react/<str:reaction_type>/", post_reaction, name="post_reaction"),
    path("posts/<int:post_id>/react/<str:reaction_type>/", post_reaction, name="post_reaction"),
    # Password Reset URLs
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"), name="password_reset_complete"),
]
