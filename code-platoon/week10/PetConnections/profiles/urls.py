from django.urls import path, include
from . import views
from .models import User_Profile,Pet_Profile,Questionaire,Match


urlpatterns=[
    path('', views.user_profile_list, 
    name='user_profile_list'),
    path('new/', views.new_user_profile, 
    name='new_user_profile'),
    path('<int:user_profile_id>/', views.user_profile_detail, name='user_profile_detail'),
    path('<int:user_profile_id>/edit', views.edit_user_profile, name='edit_user_profile'),
    path('<int:user_profile_id>/delete', views.delete_user_profile, 
    name='delete_user_profile'),

]