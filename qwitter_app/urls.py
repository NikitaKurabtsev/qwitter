from django.urls import path
from qwitter_app import views


app_name = 'qwitter_app'


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('profile_list/', views.profile_list, name='profile_list'),
    path('profile/<int:pk>/', views.profile, name='profile'),

]