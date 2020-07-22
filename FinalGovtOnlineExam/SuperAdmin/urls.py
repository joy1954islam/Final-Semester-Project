from django.urls import path

from . import views

urlpatterns = [
    path('SuperAdminHome/', views.SuperAdminHome, name='SuperAdminHome'),
    path('SuperAdminProfile/',views.SuperAdminProfile, name='SuperAdminProfile'),
    path('GovtSignUpView/',views.GovtSignUpView.as_view(), name='GovtSignUpView'),

    path('ministry/', views.ministry_list, name='ministry_list'),
    path('ministry/create/', views.ministry_create, name='ministry_create'),
    path('<int:pk>/ministry/update/', views.ministry_update, name='ministry_update'),
    path('<int:pk>/ministry/delete/', views.ministry_delete, name='ministry_delete'),

    path('govtemployee/', views.govtemployee_list, name='govtemployee_list'),
    # path('govtemployee/create/', views.govtemployee_create.as_view(), name='govtemployee_create'),
    # path('<int:pk>/govtemployee/update/', views.govtemployee_update, name='govtemployee_update'),
    path('<int:pk>/govtemployee/delete/', views.govtemployee_delete, name='govtemployee_delete'),
]