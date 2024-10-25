from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_menu_item, name='add_menu_item'),
    path('<int:pk>/delete/', views.delete_menu_item, name='delete_menu_item'),
    path('<int:pk>/update/', views.update_menu_item, name='update_menu_item'),
    path('', views.view_menu, name='view_menu'),
]
