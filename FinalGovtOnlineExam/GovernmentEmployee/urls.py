from django.contrib import admin
from django.urls import path, include

from GovernmentEmployee import views
from accounts.views import IndexPageView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('GovernmentEmployeeHome/', views.GovernmentEmployeeHome, name='GovernmentEmployeeHome'),
    path('GovernmentEmployeeProfile/', views.GovernmentEmployeeProfile, name='GovernmentEmployeeProfile'),

    path('change/password/', views.ChangePasswordView.as_view(), name='change_password'),
    path('change/email/', views.ChangeEmailView.as_view(), name='change_email'),
    path('change/email/<code>/', views.ChangeEmailActivateView.as_view(), name='change_email_activation'),

]
