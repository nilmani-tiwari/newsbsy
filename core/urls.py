from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),    
    path("login1/", views.login1, name="login1"),
    path("logout1/", auth_views.LogoutView.as_view(), name="logout1"),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path("home1", views.home1, name="home1"),
    path("policy", views.policy, name="policy"),
]