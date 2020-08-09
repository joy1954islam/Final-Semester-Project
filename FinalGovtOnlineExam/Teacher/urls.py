from django.urls import path

from Teacher import views

urlpatterns = [

    path('TeacherHome/', views.home, name='TeacherHome'),

    path('TeacherProfile/', views.TeacherProfile, name='TeacherProfile'),
    path('change/password/', views.ChangePasswordView.as_view(), name='Teacher_change_password'),
    path('change/email/', views.ChangeEmailView.as_view(), name='Teacher_change_email'),
    path('change/email/<code>/', views.ChangeEmailActivateView.as_view(), name='change_email_activation'),

]
