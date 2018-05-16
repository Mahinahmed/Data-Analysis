from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.ClientLoginView.as_view(), name='login'),
    path('index/', views.IndexView.as_view(), name='home'),
    path('sign-up/', views.SignUpView.as_view(), name='signup'),
    path('logout/', views.ClientLogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', views.ClientDetail.as_view(), name='profile')
]
