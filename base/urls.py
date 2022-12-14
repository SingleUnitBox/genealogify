from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name='logout'),
    path('family/', views.family, name='family'),
    path('add_member/', views.add_member, name="add_member"),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('delete_member/<str:pk>', views.delete_member, name="delete_member"),
    path('edit_member/<str:pk>', views.edit_member, name="edit_member"),
]