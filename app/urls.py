from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminUser, name='home'),
    path("signin",views.signin, name="signin"),
    path("login",views.login, name="login"),
    path("logout",views.logoutUser, name="logout"),
    path("upload/<int:id>",views.uploadScreenShort, name="upload"),
    path("adminHome",views.adminHome, name="adminHome"),
    path("userHome",views.userHome, name="userHome"),
    path("userPoints",views.points, name="userPoints"),
]