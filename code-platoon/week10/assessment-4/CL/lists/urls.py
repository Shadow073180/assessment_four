from django.urls import path
from . import views

urlpatterns=[
    path('', views.catagory_list, name='catagory_list'),
    path('new', views.new_catagory, name='new_catagory'),
    path('<int:catagory_id>/', views.catagory_detail, name='catagory_detail'),
    path('<int:catagory_id>/edit', views.edit_catagory, name='edit_catagory'),
    path('<int:catagory_id>/delete', views.delete_catagory, name='delete_catagory'),
]