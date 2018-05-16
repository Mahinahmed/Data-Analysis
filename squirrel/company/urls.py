from django.urls import path

from . import views

urlpatterns = [
    path('', views.CompanyListView.as_view(), name='company-list'),
    path('details/<int:pk>/', views.CompanyDetailsView.as_view(), name='company-details'),
    path('review/', views.ReviewCreateView.as_view(), name='review-create')
]
