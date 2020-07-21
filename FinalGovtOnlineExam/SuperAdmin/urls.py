from django.urls import path

from . import views

urlpatterns = [
    path('SuperAdminHome/', views.SuperAdminHome, name='SuperAdminHome'),
    path('SuperAdminProfile/',views.SuperAdminProfile, name='SuperAdminProfile'),
    path('ministry/', views.ministry_list, name='ministry_list'),
    path('ministry/create/', views.ministry_create, name='ministry_create'),
    path('<int:pk>/ministry/update/', views.ministry_update, name='ministry_update'),
    path('<int:pk>/ministry/delete/', views.ministry_delete, name='ministry_delete'),
]