from django.contrib import admin
from django.urls import path, include

from GovernmentEmployee import views
from accounts.views import IndexPageView
from django.conf import settings
from django.conf.urls.static import static
from TeacherEnroll import views as teacherEnroll

urlpatterns = [
    path('Home/', views.home, name='govt_home'),

    path('GovernmentEmployeeHome/', views.GovernmentEmployeeHome, name='GovernmentEmployeeHome'),
    path('GovernmentEmployeeProfile/', views.GovernmentEmployeeProfile, name='GovernmentEmployeeProfile'),

    path('change/password/', views.ChangePasswordView.as_view(), name='GovernmentEmployee_change_password'),
    path('change/email/', views.ChangeEmailView.as_view(), name='GovernmentEmployee_change_email'),
    path('change/email/<code>/', views.ChangeEmailActivateView.as_view(), name='change_email_activation'),

    path('course/', views.course_list, name='course_list'),
    path('course/create/', views.course_create, name='course_create'),
    path('<int:pk>/course/update/', views.course_update, name='course_update'),
    path('<int:pk>/course/view/', views.course_view, name='course_view'),
    path('<int:pk>/course/delete/', views.course_delete, name='course_delete'),

    path('content/', views.topic_list, name='topic_list'),
    path('content/create/', views.topic_create, name='topic_create'),
    path('<int:pk>/content/update/', views.topic_update, name='topic_update'),
    path('<int:pk>/content/delete/', views.topic_delete, name='topic_delete'),

    path('teacherEnroll/', teacherEnroll.teacherEnroll_list, name='teacherEnroll_list'),
    path('teacherEnroll/create/', teacherEnroll.teacherEnroll_create, name='teacherEnroll_create'),
    path('<int:pk>/teacherEnroll/update/', teacherEnroll.teacherEnroll_update, name='teacherEnroll_update'),
    path('<int:pk>/teacherEnroll/delete/', teacherEnroll.teacherEnroll_delete, name='teacherEnroll_delete'),

    path('teacher/', views.teacher_list, name='teacher_list'),
    path('teacher/create/', views.TeacherSignUpView.as_view(), name='teacher_create'),
    # path('<int:pk>/teacher/update/', views.teacher_update, name='teacher_update'),
    path('<int:pk>/teacher/delete/', views.teacher_delete, name='teacher_delete'),
    path('<int:pk>/teacher/view/', views.teacher_view, name='teacher_view'),

]
