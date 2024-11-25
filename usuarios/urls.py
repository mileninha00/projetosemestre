from django.urls import path
from .views import EditProfileView, LoginView, LogoutView, ProfileView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('editarperfil/', EditProfileView.as_view(), name='edit_profile'),
    path('perfil/', ProfileView.as_view(), name='profile'), 
]